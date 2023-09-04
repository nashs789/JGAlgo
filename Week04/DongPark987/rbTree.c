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
void colorSwap(node_t* cur); //인자 부모노드


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
		//printf("쌍빨강\n");

		colorSwap(parent,t);
		t->root->color = RBTREE_BLACK;
		return 5;
	}
	if (now == parent->left && parent == grand->left) {
		//printf("좌선형\n");

		rightTurn(now, t, 0);
		return 1;
	}

	if (now == parent->right && parent == grand->left) {
		//printf("좌꺽형\n");

		leftTurn(now, t, 1);
		rightTurn(now->left, t, 0);
		return 2;
	}
	if (now == parent->right && parent == grand->right) {
		//printf("우선형\n");

		leftTurn(now, t, 0);
		return 3;
	}
	if (now == parent->left && parent == grand->right) {
		//printf("우꺽형\n");
		
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

	//부모의 우측 => 조부
	//printf("%d의 우측 = %d\n", parent->key, grand->key);
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

	//부모의 부모 => 조부의 부모
	parent->parent = grand->parent;
	//조부의 부모 => 부모
	grand->parent = parent;
	//조부의 우측 => 부모의 좌측
	grand->right = parent->left;

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

	if (t->root == NULL) {
		newNode->color = RBTREE_BLACK;
		newNode->parent = NULL;
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
				checkCase(newNode,t);
				return t->root;

			}
		}
		else {
			if (cur->right != NULL) {
				cur = cur->right;
			}
			else {
				cur->right = newNode;
				newNode->parent = cur;
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

	return 0;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
  // TODO: implement to_array
  return 0;
}


int cnt;
void rbPrint(node_t* root) {
	cnt++;


	printf("번호: %d, 출력: %d, 색상: %d", cnt, root->key, root->color);    // 루트노드 방문
	if (root->left == NULL) {
		printf(" 좌자식: %d", -1);
	}
	else {
		printf(" 좌자식: %d", root->left->key);

	}
	if (root->right == NULL) {
		printf(" 우자식: % d\n", -1);
	}
	else {
		printf(" 우자식: %d\n", root->right->key);

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
	rbtree_erase(p, find);

}

int main() {
	rbtree* R = new_rbtree();
	printf("%d", R->root);


	int num[] = { 99,45,1000,8,32,22,843,4123,5345,6777,788,2,0,9 };
	int num2[] = {1,10,25,9,-55,13,60};

	for (int i = 0; i <= 6; i++) {
		printf("\n");
		rbtree_insert(R, num2[i]);
		cnt = 0;
		rbPrint(R->root);
	}
	return 0;
}
