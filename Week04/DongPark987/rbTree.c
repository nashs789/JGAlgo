#include "rbtree.h"
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

rbtree *new_rbtree(void) {
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  // TODO: initialize struct if needed
  return p;
}

void rightTurn(node_t* now, rbtree* t, int mode);
void leftTurn(node_t* now, rbtree* t, int mode);
void colorSwap(node_t* cur); //인자 부모노드rbPrint
int cnt;
int cnt2;
void rbPrint(node_t* root);

void delete_node(node_t* N) {
	if (N->left != NULL) {
		delete_node(N->left);
	}
	if (N->right != NULL) {
		delete_node(N->right);
	}
	free(N);
}

void delete_rbtree(rbtree* t) {
	// TODO: reclaim the tree nodes's memory
	delete_node(t->root);
	free(t);
}

int checkCase(node_t* now, rbtree* t) {
	if (now->parent == NULL) return -1;
	node_t* parent = now->parent;
	node_t* grand = parent->parent;

	if (parent->color == RBTREE_BLACK)
		return 0;
	//케이스1 좌선형
	if (grand->right != NULL && grand->left != NULL && grand->right->color == RBTREE_RED && grand->left->color == RBTREE_RED) {
		printf("쌍빨강\n");
		colorSwap(parent,t);
		t->root->color = RBTREE_BLACK;
		return 5;
	}
	if (now == parent->left && parent == grand->left) {
		printf("좌선형\n");
		rightTurn(now, t, 0);
		return 1;
	}

	if (now == parent->right && parent == grand->left) {
		printf("좌꺽형\n");
		leftTurn(now, t, 1);
		rightTurn(now->left, t, 0);
		return 2;
	}
	if (now == parent->right && parent == grand->right) {
		printf("우선형\n");
		leftTurn(now, t, 0);
		return 3;
	}
	if (now == parent->left && parent == grand->right) {
		printf("우꺽형\n");
		rightTurn(now, t, 1);
		leftTurn(now->right, t, 0);
		return 4;
	}
}

void colorSwap(node_t* cur, rbtree* t) {
	if (cur->parent == NULL) {
		cur->color = RBTREE_BLACK;
		return;
	}
	
	node_t* parent = cur->parent;
	node_t* pLeft = parent->left;
	node_t* pRight = parent->right;
	//printf("쌍빨강 부모:%d\n", parent->key);

	if (pRight->color == RBTREE_RED && pLeft->color == RBTREE_RED) {
		parent->color = RBTREE_RED;
		//printf("%d의 색 빨간색으로\n", parent->key);
		//printf("%d의 색 검은색으로\n", pRight->key);
		//printf("%d의 색 검은색으로\n", pLeft->key);
		pRight->color = RBTREE_BLACK;
		pLeft->color = RBTREE_BLACK;
		node_t* grand = parent->parent;

		if (grand != NULL && grand->left->color == RBTREE_RED && grand->right == RBTREE_RED) {
			//printf("색변환 재귀\n");
			colorSwap(parent, t);
		}
	}
	checkCase(parent, t);
}

void rightTurn(node_t* now, rbtree *t, int mode) {
	node_t* parent = NULL;
	node_t* grand = NULL;
	if (mode == 0) {
		parent = now->parent;
		grand = parent->parent;
	}
	else {
		parent = now;
		grand = now->parent;
	}

	//부모의 부모 => 조부의 부모
	parent->parent = grand->parent;
	//조부의 부모 => 부모
	grand->parent = parent;
	//조부의 좌측 => 부모의 우측
	grand->left = parent->right;
	if (parent->right != NULL)
		parent->right->parent = grand;
	//부모의 우측 => 조부
	parent->right = grand;

	//부모 조부 색상 스와핑
	if (mode == 0) {
		//printf("우회전 색상 스와핑 %d 색:%d <---> %d 색:%d \n",parent->key,parent->color,grand->key,parent->color);
		color_t tmp = parent->color;
		parent->color = grand->color;
		grand->color = tmp;
	}
	//루트로 변경된 경우
	if (parent->parent == NULL) {
		t->root = parent;
	}
	else {
		if (parent->parent->left == grand) {
			parent->parent->left = parent;
		}
		else {
			parent->parent->right = parent;
		}
	}
}


void leftTurn(node_t* now, rbtree* t, int mode) {
	node_t* parent = NULL;
	node_t* grand = NULL;
	if (mode == 0) {
		parent = now->parent;
		grand = parent->parent;
	}
	else {
		parent = now;
		grand = now->parent;
	}
	printf("좌회전, 부모%d, 조부%d, 조조부\n", parent->key, grand->key);
	//부모의 부모 => 조부의 부모
	parent->parent = grand->parent;
	//조부의 부모 => 부모
	grand->parent = parent;
	//조부의 우측 => 부모의 좌측
	grand->right = parent->left;
	if(parent->left!=NULL)
		parent->left->parent = grand;

	//부모의 좌측 => 조부
	//printf("좌회전 %d의 우측 = %d\n", parent->key, grand->key);
	parent->left = grand;
	
	//부모 조부 색상 스와핑
	if (mode == 0) {
		color_t tmp = parent->color;
		parent->color = grand->color;
		grand->color = tmp;
	}
	//루트로 변경된 경우
	if (parent->parent == NULL) {
		t->root = parent;
	}
	else {
		if (parent->parent->left == grand) {
			//printf("좌회전 색상 스와핑 %d 색:%d <---> %d 색:%d \n", parent->key, parent->color, grand->key, parent->color);

			parent->parent->left = parent;
		}
		else {
			parent->parent->right = parent;
		}
	}
}

node_t* rbtree_insert(rbtree* t, const key_t key) {
	// TODO: implement insert
	//printf("%d 추가\n", key);
	node_t* newNode = (node_t*)malloc(sizeof(node_t));
	newNode->color = RBTREE_RED;
	newNode->key = key;
	newNode->parent = NULL;
	newNode->left = NULL;
	newNode->right = NULL;
	newNode->data = cnt2;

	if (t->root == NULL) {
		newNode->color = RBTREE_BLACK;
		newNode->parent = t->root;
		t->root = newNode;
		return t->root;
	}

	node_t* cur = t->root;
	while (cur != NULL) {
		if (key <= cur->key) {
			if (cur->left != NULL) {
				cur = cur->left;
			}
			else {
				newNode->parent = cur;
				cur->left = newNode;
				//printf("회전 전\n");
				//cnt = 0;
				//rbPrint(t);
				//printf("\n");
				checkCase(newNode,t);
				return t->root;

			}
		}
		else {
			if (cur->right != NULL) {
				cur = cur->right;
			}
			else {
				newNode->parent = cur;
				cur->right = newNode;
				//printf("회전 전\n");
				//cnt = 0;
				//rbPrint(t);
				//printf("\n");

				checkCase(newNode,t);
				return t->root;

			}
		}
	}

	return t->root;
}

node_t* rbtree_find(const rbtree* t, const key_t key) {
	// TODO: implement find
	node_t *cur = t->root;

	while (cur != NULL) {
		if (cur->key == key) {
			return cur;
		}
		if (key <= cur->key) {
			cur = cur->left;
		}
		else {
			cur = cur->right;
		}
	}

	return NULL;
}

node_t *rbtree_min(const rbtree *t) {
  // TODO: implement find
  return t->root;
}

node_t *rbtree_max(const rbtree *t) {
  // TODO: implement find
  return t->root;
}

int rbtree_erase(rbtree* t, node_t* p) {
	// TODO: implement erase

	node_t* cur = p;

	//우측 우선으로 자식이 있는지 확인
	if (cur->right != NULL) {
		cur = cur->right;
		while (cur->left != NULL)
			cur = cur->left;
		//cur은 우측에서 가장 작은 값
		p->key = cur->key;
		if(cur->parent->right == cur)
			cur->parent->right = cur->right;
		else
			cur->parent->left = cur->right;
	}
	else {
		if (cur->parent->right == cur)
			cur->parent->right = cur->left;
		else
			cur->parent->left = cur->left;
	}
	free(cur);
	return 0;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
  // TODO: implement to_array
  return 0;
}


void rbPrint(node_t* root) {
	cnt++;


	printf("번호:%d cnt:%d  출력: %d, 색상: %d",cnt,root->data, root->key, root->color);    // 루트노드 방문
	if (root->left == NULL) {
		printf(" 좌자식: %d", -1);
	}
	else {
		printf(" 좌자식: %d", root->left->key);

	}
	if (root->right == NULL) {
		printf(" 우자식: %d", -1);
	}
	else {
		printf(" 우자식: %d", root->right->key);

	}

	if (root->parent == NULL) {
		printf(" 부모: root\n");
	}
	else {
		printf(" 부모: %d\n",root->parent->data);

	}


	if (root->left != NULL)
		rbPrint(root->left);    // 왼쪽 서브트리
	//cnt--;
	//printf("번호: %d, 출력: %d\n",cnt,root->key);    // 루트노드 방문
	//cnt++;
	if (root->right != NULL)
		rbPrint(root->right);    // 오른쪽 서브트리

}

void deleteOne(rbtree* p, int key) {
	node_t* find = rbtree_find(p, key);
	printf("파인드: %d\n", find->key);
	rbtree_erase(p, find);
}

int main() {
	rbtree* R = new_rbtree();


	int num[] = { 99,45,1000,8,32,22,843,4123,5345,6777,788,2,0,9 };
	int num2[] = {1,10,25,9,-55,13,60};
	//int num3[] = { 10,10,10,22,30,100,23,22,-199,22,22 };
	int num3[] = { 1,2,3,4,5,6,7,8,9,10 };
	//int num3[] = { 5,1,3 };
	int num4[] = { 1,2,4,10,10,10,10,10,10 };
	//int num4[] = { 10,10,10,10,1,12,13,10,10 };

	int size = 10;
	cnt2 = 0;
	for (int i = 0; i <size; i++) {
		cnt2 = i;
		printf("\n");
		printf("%d 입력\n", num3[i]);
		rbtree_insert(R, num3[i]);
		cnt = 0;
		rbPrint(R->root);
	}

	deleteOne(R,6);
	printf("\n");
	cnt = 0;
	rbPrint(R->root);
	
	return 0;
}
