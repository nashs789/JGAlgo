#include "rbtree.h"

#include <stdlib.h>
#include <stdio.h>

void rbtree_fixup(rbtree *t, node_t **node);
void right_rotate(rbtree *t, node_t **x);
void left_rotate(rbtree *t, node_t **x);
void delete_node(rbtree *t, node_t *node);

rbtree *new_rbtree(void) {
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  node_t *trash = (node_t *)calloc(1, sizeof(node_t));
  
  // TODO: initialize struct if needed
  p->nil = trash;
  p->root = p->nil;
  return p;
}

void delete_rbtree(rbtree *t) {
  // TODO: reclaim the tree nodes's memory

  if (t->root != t->nil) {
    delete_node(t, t->root);
  } else {
    printf("^-^");
    free(t->root);
  }

  free(t->nil);
  free(t);
}

void delete_node(rbtree *t, node_t *node) {
  if (node->left != t->nil) {
    delete_node(t, node->left);
  }
  if (node->right != t->nil) {
    delete_node(t, node->right);
  }
  free(node);
}

node_t *rbtree_insert(rbtree *t, const key_t key) {
  node_t *new_node = (node_t *)calloc(1, sizeof(node_t));
  new_node->key = key;
  new_node->color = RBTREE_RED;
  new_node->parent = t->nil;
  new_node->left = t->nil;
  new_node->right = t->nil;

  node_t *now = t->root;

  if(t->root==t->nil){
    t->root = new_node;
    new_node->color = RBTREE_BLACK;
    return t->root;
  }

  while (now != t->nil) {
    new_node->parent = now;
    if (key < now->key) {
      if (now->left == t->nil) {
        now->left = new_node;
        break;
      } else {
        now = now->left;
      }
    } else {
      if (now->right == t->nil) {
        now->right = new_node;
        break;
      } else {
        new_node->parent = now->right;
        now = now->right;
      }
    }
  }
  
  if (now->color == RBTREE_RED) {
    rbtree_fixup(t, &new_node);
  }
  return t->root;
}

void rbtree_fixup(rbtree *t, node_t **node) {
  while ((*node)->parent != t->nil && (*node)->color == RBTREE_RED) {
    node_t* p = (*node)->parent;
    if (p->parent == t->nil || (*node)->parent->color == RBTREE_BLACK) { 
      break;
    }
    node_t* g = p->parent;  
    node_t* u = t->nil;

    if (p == g->left) {
        u = g->right;

      if (u != t->nil && u->color == RBTREE_RED) {
        g->color = !(g->color);
        u->color = !(u->color);
        p->color = !(p->color);
        *node = g;
      } else { // 삼촌이 nil이거나 블랙일 경우 
        if ( (*node) == p->right) { //트라이앵글 (부모방향 내방향이랑 다름)
          *node = p;
          left_rotate(t, node);
          p = (*node)->parent;
        }
        if (*node != p) {
          *node = p;
        }
        p->color = !(p->color);
        g->color = !(g->color);
        right_rotate(t, &g);
      }
    } else { // p가 g의 오른쪽 자식일 경우
      u = g->left;
      if (u != t->nil && u->color == RBTREE_RED) {
        g->color = !(g->color);
        u->color = !(u->color);
        p->color = !(p->color);
        *node = g;
      } else { // 삼촌이 nil이거나 블랙일 경우
        if ( (*node) == p->left) { //트라이앵글 (부모방향 내방향이랑 다름)
          *node = p;
          right_rotate(t, node);
          p = (*node)->parent;
        }
        if (*node != p) {
          *node = p;
        }
        p->color = !(p->color);
        g->color = !(g->color);
        left_rotate(t, &g);
      }
    } 
  } 
  t->root->color = RBTREE_BLACK;
}

void left_rotate(rbtree *t, node_t **x) {
  node_t* y = (*x)->right;

  (*x)->right = y->left;
  if (y->left != t->nil) {
    y->left->parent = *x;
  }

  y->parent = (*x)->parent;
  if ((*x)->parent == t->nil) {
    t->root = y;
  } else if ((*x)==(*x)->parent->left){
    (*x)->parent->left = y;
  } else {
    (*x)->parent->right = y;
  }
  y->left = *x;
  (*x)->parent = y;
}

void right_rotate(rbtree *t, node_t **x) {
  node_t* y = (*x)->left;
  (*x)->left = y->right;
  if (y->right != t->nil) {
    y->right->parent = *x;
  }

  y->parent = (*x)->parent;
  if ((*x)->parent == t->nil) {
    t->root = y;
  } else if ((*x) == (*x)->parent->left){
    (*x)->parent->left = y;
  } else {
    (*x)->parent->right = y;
  }

  y->right = *x;
  (*x)->parent = y;
}


node_t *rbtree_find(const rbtree *t, const key_t key) {
  // TODO: implement find
  return t->root;
}

node_t *rbtree_min(const rbtree *t) {
  // TODO: implement find
  return t->root;
}

node_t *rbtree_max(const rbtree *t) {
  // TODO: implement find
  return t->root;
}

int rbtree_erase(rbtree *t, node_t *p) {
  // TODO: implement erase
  return 0;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
  // TODO: implement to_array
  return 0;
}

void print_tree(rbtree *t, node_t *now) {
  if (now->left != t->nil) {
    print_tree(t, now->left);
  }
  printf("현재 노드는 %d, %d 입니다  ", now->key, now->color);
  if (now->left != t->nil) {
    printf("왼쪽은 %d   ", now->left->key);
  }
  if (now->right != t->nil) {
    printf("오른쪽은 %d   ", now->right->key);
  }
  printf("\n");
  if (now->right != t->nil) {
    print_tree(t, now->right);
  }
}

int main() {
 rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));

  int num[] = { 2,2,2,2,2,2,843,4123,5345,6777,788,2,0,9 };
	for (int i = 0; i <= 5; i++) {
		rbtree_insert(p, num[i]);
  }

  print_tree(p, p->root);
  printf("%d\n", p->root->key);
}
