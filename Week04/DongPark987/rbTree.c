#include "rbtree.h"
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <assert.h>
rbtree *new_rbtree(void) {
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  return p;
}

void rightTurn(node_t* now, rbtree* t, int mode);
void leftTurn(node_t* now, rbtree* t, int mode);
void colorSwap(node_t* cur, rbtree *t); //인자 부모노드rbPrint
int c_c(node_t* p);
node_t* get_node(node_t* p);
int cnt;
int cnt2;
void rbPrint(node_t* root);

void delete_node(node_t* N) {
	if (N == NULL) {
		return;
	}
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
	//printf("좌회전, 부모%d, 조부%d, 조조부\n", parent->key, grand->key);
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
	node_t* newNode = (node_t*)malloc(sizeof(node_t));
	newNode->color = RBTREE_RED;
	newNode->key = key;
	newNode->parent = NULL;
	newNode->left = NULL;
	newNode->right = NULL;

	if (t->root == NULL) {
		newNode->color = RBTREE_BLACK;
		newNode->parent = t->root;
		t->root = newNode;
		return t->root;
	}

	node_t* cur = t->root;
	while (cur != NULL) {
		if (key < cur->key) {
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
				newNode->parent = cur;
				cur->right = newNode;
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
		if (key < cur->key) {
			cur = cur->left;
		}
		else {
			cur = cur->right;
		}
	}

	return NULL;
}

node_t* rbtree_min(const rbtree* t) {
	// TODO: implement find
	node_t* cur = t->root;
	if (cur->left == NULL)
		return cur;
	while (cur->left != NULL)
		cur = cur->left;

	return cur;
}

node_t *rbtree_max(const rbtree *t) {
  // TODO: implement find
	node_t* cur = t->root;
	if (cur->right == NULL)
		return cur;
	while (cur->right != NULL)
		cur = cur->right;

	return cur;
}

void delete_check(rbtree* t, node_t* x, int LR) {
	node_t* p = x->parent; //부모
	node_t* s = NULL; //형제
	node_t* l = NULL; //형자왼
	node_t* r = NULL; //형자우
	//좌측
	if (LR == 0) {
		//printf("좌측\n");
		s = (p->right);
		if (s != NULL) {
			l = s->left;
			r = s->right;
		}

		//case 1-1, parent: 레드, sibling: 블랙 =>  <블랙, 블랙>
		//printf("x:%d, p:%d, s:%d, l:%d, r:%d\n", x->color, p->color, s->color, c_c(l), c_c(r));
		if (p->color == 0 && c_c(s) == 1 && c_c(l) == 1 && c_c(r) == 1) {
			//printf("case 1-1\n");
			p->color = 1;
			if (s != NULL)
				s->color = 0;
			return;
		}
		
		//case *-2, parent: *, sibling: 블랙 =>  <*, 레드>
		if (c_c(s) == 1 && c_c(r) == 0) {
			//printf("case *-2\n");
			leftTurn(s, t, 1);
			int tmp = p->color;
			p->color = s->color;
			s->color = tmp;
			r->color = 1;
			return;
		}

		//case *-3, parent: *, sibling: 블랙 =>  <레드,블랙>
		if (c_c(s) == 1 && c_c(l) == 0 && c_c(r) == 1) {
			//printf("case *-3\n");
			rightTurn(s->left, t, 1);
			int tmp = s->color;
			s->color = l->color;
			l->color = tmp;
			delete_check(t, x, LR);
			return;
		}

		//case 2-1, parent: 블랙, sibling: 블랙 =>  <블랙,블랙>
		if (p->color==1 && c_c(s) == 1 && c_c(l) == 1 && c_c(r) == 1) {
			//printf("case 2-1\n");
			if(s!=NULL)
				s->color = 0;
			if (p->parent == NULL)
				return;
			if (p->parent->left == p)
				delete_check(t, p, 0);
			else 
				delete_check(t, p, 1);
			return;
		}

		//case 2-4, parent: 블랙, sibling:레드 =>  <블랙,블랙>
		if (p->color == 1 && c_c(s) == 0 && c_c(l) == 1 && c_c(r) == 1) {
			//printf("case 2-4\n");
			leftTurn(s, t, 1);
			p->color = 0;
			s->color = 1;
			delete_check(t, x, LR);
			return;
		}


	}
	//우측
	else {
		//printf("우측\n");
		s = get_node(p->left);
		if (s != NULL) {
			l = s->left;
			r = s->right;
		}
		//case 1-1, parent: 레드, sibling: 블랙 =>  <블랙, 블랙>
		//printf("x:%d, p:%d, s:%d, l:%d, r:%d\n", x->color, p->color, s->color, c_c(l), c_c(r));
		if (p->color == 0 && c_c(s) == 1 && c_c(l) == 1 && c_c(r) == 1) {
			//printf("case 1-1\n");
			p->color = 1;
			if (s != NULL)
				s->color = 0;
			return;
		}

		//case *-2, parent: *, sibling: 블랙 =>  <*, 레드>
		if (c_c(s) == 1 && c_c(l) == 0) {
			//printf("case *-2\n");
			rightTurn(s, t, 1);
			int tmp = p->color;
			p->color = s->color;
			s->color = tmp;
			l->color = 1;
			return;
		}

		//case *-3, parent: *, sibling: 블랙 =>  <레드,블랙>
		if (c_c(s) == 1 && c_c(r) == 0 && c_c(l) == 1) {
			//printf("case *-3\n");
			leftTurn(s->right, t, 1);
			s->color = 0;
			r->color = 1;
			delete_check(t, x, LR);
			return;
		}

		//case 2-1, parent: 블랙, sibling: 블랙 =>  <블랙,블랙>
		if (p->color == 1 && c_c(s) == 1 && c_c(l) == 1 && c_c(r) == 1) {
			//printf("case 2-1\n");
			if (s != NULL)
				s->color = 0;
			if (p->parent == NULL)
				return;
			if (p->parent->left == p)
				delete_check(t, p, 0);
			else
				delete_check(t, p, 1);
			return;
		}

		//case 2-4, parent: 블랙, sibling:레드 =>  <블랙,블랙>
		if (p->color == 1 && c_c(s) == 0 && c_c(l) == 1 && c_c(r) == 1) {
			//printf("case 2-4\n");
			rightTurn(s, t, 1);
			p->color = 0;
			s->color = 1;
			delete_check(t, x, LR);
			return;
		}
	}
}

int c_c(node_t* p) {
	if (p == NULL) {
		return 1;
	}
	else {
		return p->color;
	}
}

node_t* get_node(node_t* p) {
	if (p == NULL) {
		return NULL;
	}
	else {
		return p;
	}
}

int rbtree_erase(rbtree* t, node_t* p) {
	// TODO: implement erase

	node_t* cur = p;
	//printf("%d delete\n", p->key);

	//왼쪽 자식이 있음
	if (cur->left != NULL) {
		cur = cur->left;
		while (cur->right != NULL) {
			cur = cur->right;
			//printf("loop %d\n",cur->key);
		}
	}
	//왼쪽 자식이 없음
	else if (cur->right != NULL) {
		cur = cur->right;
	}

	//cur == 삭제할 노드
	//printf("삭제할 노드 선택 %d\n", cur->key);
	key_t tmp_key = p->key;
	p->key = cur->key;
	cur->key = tmp_key;
	//쉬운 삭제 케이스1, 삭제노드가 레드
	//printf("좌자식 색:%d, 우좌식 색: %d\n", c_c(cur->left), c_c(cur->right));
	if (cur->color == RBTREE_RED) {
		printf("쉬삭케1\n");
		if (cur->parent->left == cur)
			cur->parent->left = cur->left;
		else
			cur->parent->right = cur->right;

		if (cur->left != NULL)
			cur->left->parent = cur->parent;
		free(cur);
		return 0;
	}
	//쉬운 삭제 케이스2, 삭제노드는 블랙, 자식중 하나가 레드
	else if (c_c(cur->left) == RBTREE_RED || c_c(cur->right) == RBTREE_RED) {
		printf("쉬삭케2\n");
		if (cur->parent->left == cur)
			cur->parent->left = cur->left;
		else
			cur->parent->right = cur->left;
		if (cur->left != NULL) {
			cur->left->parent = cur->parent;
			cur->left->color = RBTREE_BLACK;
		}
		free(cur);
		return 0;
	}
	//printf("안쉬삭케\n");
	int LR = 0;
	if (cur->parent != NULL) {
		if (cur->parent->left == cur) {
			cur->parent->left = cur->left;
			LR = 0;
		}
		else {
			cur->parent->right = cur->left;
			LR = 1;
		}

		if (cur->left != NULL)
			cur->left->parent = cur->parent;
		delete_check(t, cur, LR);
	}
	else {
		t->root = NULL;
	}
	free(cur);
	
	return 0;



	/*
	if (cur->left  != NULL) {
		cur = cur->left;
		while (cur->right != NULL)
			cur = cur->right;
		//cur은 우측에서 가장 작은 값
		p->key = cur->key;
		
	}
	else {
		if (cur->parent->left == cur)
			cur->parent->left = cur->right;
		else
			cur->parent->right = cur->right;
	}
	*/

}
int arrCnt;

void inorder(node_t* N, key_t* arr, const size_t n) {
	if (N == NULL || arrCnt == n) {
		return;
	}
	if (N->left != NULL) {
		inorder(N->left, arr, n);
	}
	arr[arrCnt] = N->key;
	arrCnt++;
	if (N->right != NULL) {
		inorder(N->right, arr, n);
	}

	
}

int rbtree_to_array(const rbtree* t, key_t* arr, const size_t n) {
	// TODO: implement to_array
	inorder(t->root, arr, n);

	return 0;
}


void rbPrint(node_t* root) {
	cnt++;
	if (root == NULL)
		return;

	printf("번호:%d 출력: %d, 색상: %d",cnt, root->key, root->color);    // 루트노드 방문
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
		printf(" 부모: %d\n",root->parent->key);

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
	//printf("파인드: %d\n", find->key);
	rbtree_erase(p, find);
}



void test_find_erase(rbtree* t, const key_t* arr, const size_t n) {
	for (int i = 0; i < n; i++) {
		node_t* p = rbtree_insert(t, arr[i]);
		assert(p != NULL);
	}
	printf("\n");

	for (int i = 0; i < n; i++) {
		node_t* p = rbtree_find(t, arr[i]);
		// printf("arr[%d] = %d\n", i, arr[i]);
		assert(p != NULL);
		assert(p->key == arr[i]);
		rbtree_erase(t, p);
	}

	for (int i = 0; i < n; i++) {
		node_t* p = rbtree_find(t, arr[i]);
		assert(p == NULL);
	}

	for (int i = 0; i < n; i++) {
		node_t* p = rbtree_insert(t, arr[i]);
		assert(p != NULL);
		node_t* q = rbtree_find(t, arr[i]);
		assert(q != NULL);
		assert(q->key == arr[i]);
		assert(p == q);
		rbtree_erase(t, p);
		q = rbtree_find(t, arr[i]);
		assert(q == NULL);
	}
}
void myTest(rbtree* t, key_t* arr, size_t n);
void test_find_erase_rand(const size_t n, const unsigned int seed) {
	srand(seed);
	rbtree* t = new_rbtree();
	key_t* arr = calloc(n, sizeof(key_t));
	for (int i = 0; i < n; i++) {
		arr[i] = rand();
	}

	test_find_erase(t, arr, n);
	//myTest(t, arr, n);

	//free(arr);
	//delete_rbtree(t);
}

void myTest(rbtree *t,key_t *arr,size_t n) {
	for (int i = 0; i < n; i++) {
		rbtree_insert(t, arr[i]);
	}
	rbPrint(t->root);
}

int main() {
	rbtree* R = new_rbtree();


	//int num[] = { 99,45,1000,8,32,22,843,4123,5345,6777,788,2,0,9 };
	int num[] = { 1,2,3,4,5,6,7,8,9,10,11,12 ,0 };
	int num2[] = { 1,10,25,9,-55,13,60 };
	//int num3[] = { 10,10,10,22,30,100,23,22,-199,22,22 };
	//int num3[] = { 1,2,3,4,5,6,7,8,9,10 };
	//int num3[] = { 5,1,3 };
	int num4[] = { 1,2,4,10,10,10,10,10,10 };
	//int num4[] = { 10,10,10,10,1,12,13,10,10 };
	int num3[] = { 10,5,8,34,67,23,156,24,2,12,24,36,990,25 };
	int size = 14;
	//cnt2 = 0;
	//for (int i = 0; i < size; i++) {
	//	cnt2 = i;
	//	printf("\n");
	//	//printf("%d 입력\n", num[i]);
	//	rbtree_insert(R, num3[i]);
	//	cnt = 0;
	//	rbPrint(R->root);
	//}

	//printf("\n");

	//int arr[100];
	//rbtree_to_array(R, arr, size);

	//for (int i = 0; i < size; i++) {
	//	printf("%d, ", arr[i]);
	//}

	//for (int i = 0; i < size; i++) {
	//	printf("%d 삭제\n", num3[i]);
	//	deleteOne(R, num3[i]);
	//	printf("\n");
	//	cnt = 0;
	//	rbPrint(R->root);
	//}

	for(int i = 100; i<120;i++)
		test_find_erase_rand(20000, i);

	printf("종료\n");
	return 0;
}
