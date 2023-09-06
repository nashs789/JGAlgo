#include "rbtree.h"
#include <stdlib.h>
#include <stdio.h>

void rbtree_fixup(rbtree *t, node_t *node);
void right_rotate(rbtree *t, node_t *x);
void left_rotate(rbtree *t, node_t *x);
void delete_node(rbtree *t, node_t *node);
void delete_fixup(rbtree *t, node_t *now, int dir);

rbtree *new_rbtree(void) {
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  node_t *nil = (node_t *)calloc(1, sizeof(node_t));
  nil->color = RBTREE_BLACK;
  p->nil = nil;
  p->root = p->nil;
  return p;
}

void delete_rbtree(rbtree *t) {
  // TODO: reclaim the tree nodes's memory
  if (t->root != t->nil) {
    delete_node(t, t->root);
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
    rbtree_fixup(t, new_node);
  }
  return t->root;
}

void rbtree_fixup(rbtree *t, node_t *node) {
  while ((node)->parent != t->nil && (node)->color == RBTREE_RED) {
    node_t* p = (node)->parent;
    if (p->parent == t->nil || (node)->parent->color == RBTREE_BLACK) { 
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
        node = g;
      } else { // 삼촌이 nil이거나 블랙일 경우 
        if ( (node) == p->right) { //트라이앵글 (부모방향 내방향이랑 다름)
          node = p;
          left_rotate(t, node);
          p = (node)->parent;
        }
        if (node != p) {
          node = p;
        }
        p->color = !(p->color);
        g->color = !(g->color);
        right_rotate(t, g);
      }
    } else { // p가 g의 오른쪽 자식일 경우
      u = g->left;
      if (u != t->nil && u->color == RBTREE_RED) {
        g->color = !(g->color);
        u->color = !(u->color);
        p->color = !(p->color);
        node = g;
      } else { // 삼촌이 nil이거나 블랙일 경우
        if ( (node) == p->left) { //트라이앵글 (부모방향 내방향이랑 다름)
          node = p;
          right_rotate(t, node);
          p = (node)->parent;
        }
        if (node != p) {
          node = p;
        }
        p->color = !(p->color);
        g->color = !(g->color);
        left_rotate(t, g);
      }
    } 
  } 
  t->root->color = RBTREE_BLACK;
}

void left_rotate(rbtree *t, node_t *x) {
  node_t* y = (x)->right;

  (x)->right = y->left;
  if (y->left != t->nil) {
    y->left->parent = x;
  }

  y->parent = (x)->parent;
  if ((x)->parent == t->nil) {
    t->root = y;
  } else if ((x)==(x)->parent->left){
    (x)->parent->left = y;
  } else {
    (x)->parent->right = y;
  }
  y->left = x;
  (x)->parent = y;
}

void right_rotate(rbtree *t, node_t *x) {
  node_t* y = (x)->left;
  (x)->left = y->right;
  if (y->right != t->nil) {
    y->right->parent = x;
  }

  y->parent = (x)->parent;
  if ((x)->parent == t->nil) {
    t->root = y;
  } else if ((x) == (x)->parent->left){
    (x)->parent->left = y;
  } else {
    (x)->parent->right = y;
  }

  y->right = x;
  (x)->parent = y;
}


node_t *rbtree_find(const rbtree *t, const key_t key) {
  node_t* now = t->root;
  
  while (now != t->nil) {
    int now_value = now->key;
    if (key == now_value) {
      return now;
    }

    if (key < now_value) {
      now = now -> left;
    } else {
      now = now -> right;
    }
  }  

  return NULL;
}

node_t *rbtree_min(const rbtree *t) {
  node_t* now = t->root;

  while (now != t->nil) {
    now = now -> left;
  }

  return now;
}

node_t *rbtree_max(const rbtree *t) {
  node_t* now = t->root;

  while (now != t->nil) {
    now = now -> right;
  }
  
  return now;
}

int rbtree_erase(rbtree *t, node_t *p) {
  node_t* target = p;
  node_t* target_parent = p->parent;  

  if (target_parent == t->nil && p->left == t-> nil && p->right == t->nil) {
    free(target);
    t->root = t->nil;
    return 0;
  }

  int direction = 0; // 0: 왼쪽, 1: 오른쪽
  if (p->left != t->nil) {     //왼쪽에서 가장 큰 값을 올릴거야
    target_parent = target;
    target = target->left;
    printf("%d\n",target_parent->key);

    int isFirst = 1;
    while (target->right != t->nil) {
      isFirst=0;
      target_parent = target;
      target = target->right;
    } 
    p->key = target->key;
    if (isFirst) {
      target_parent->left = target->right;
      target->right->parent = target_parent;
    }
    else {
      target_parent->right = target->left;
      target->left->parent = target_parent;
      direction = 1;
    }
  } else { //왼쪽 자식이 없으면...? 오른쪽을 그대로 올리면 된다..
    //   target_parent = target;
    //   target = target->right;
    //   p->key = target->key;
    // if (target_parent == t->root) {
    //     t->root 
    // }

    if (target_parent->left == target) {
      printf("!!!!!!!!");
      p->key = target->right->key;
      target_parent->left = target->right;
      target->right->parent = target_parent;
      target=target->right;
    }
		else{
      printf("@@@@@@@");
      p->key = target->right->key;
      target_parent->right = target->right;
      target->right->parent = target_parent;
      target= target->right;
      direction = 1;
    } 
      
  }
  
  if (target->color == RBTREE_BLACK) {
    if (target->left != t-> nil && target->right == t->nil && target->left->color == RBTREE_RED) {
      target->left->color = !(target->left->color);
    }
    else if (target->right != t-> nil && target->left == t->nil && target->right->color == RBTREE_RED) {
      target->right->color = !(target->right->color);
    } else{
      delete_fixup(t, target, direction);
    }
  }else {
    printf("지우는게 레드임");
  }

  free(target);
  if (t->root != t->nil) {
    t->root->color = RBTREE_BLACK;
  }
  return 0;
}

void delete_fixup(rbtree *t, node_t *now, int dir) {
  if (now == t->root) {
    return;
  }

  printf("fixup함수입니다\n");

  node_t* parent = now->parent;
  node_t* s = t->nil;
  if (dir) { // dir이 1이면 오른쪽이라는 뜻, 형제는 왼쪽임
    s = parent->left;
  } else {
    s = parent->right;
  }

  printf("!!형제는 %d\n", s->key);
  printf("방향은%d\n", dir);
  node_t* l = s->left;
  node_t* r = s->right;
  if (!dir) { //왼
    // 케이스 1-1
    if (parent->color == RBTREE_RED && s->color == RBTREE_BLACK && l->color == RBTREE_BLACK && r->color == RBTREE_BLACK) {
      printf("케이스 1-1 (왼)\n");
      parent->color = !(parent->color);
      s->color = !(s->color);
      return;
    }

    if (s->color == RBTREE_BLACK) {
      // if (s->color == RBTREE_BLACK && l->color == RBTREE_RED && r->color == RBTREE_BLACK) {
      if (l->color == RBTREE_RED && r->color == RBTREE_BLACK) {
        printf("케이스 *-3 (왼)\n");
        right_rotate(t, s);
        int tmp_color = l->color;
        l->color = s->color;
        s->color = tmp_color;
      } 
      if(r->color == RBTREE_RED) {
        printf("케이스 *-2 (왼)\n"); 
        //p를 중심으로 왼쪽으로 회전
        left_rotate(t, parent);

        //p와 s의 색깔을 바꿈
        int tmp_color = parent->color;
        parent->color = s->color;
        s->color = tmp_color;

        //r을 레드에서 블랙으로
        r->color = !(r->color);
        return;
      } 
    }

    //케이스 2-1
    if (parent->color == RBTREE_BLACK && s->color == RBTREE_BLACK && l->color == RBTREE_BLACK && r->color == RBTREE_BLACK) { 
      printf("케이스 2-1 (왼)\n");
      s->color = !(s->color);
      if (parent->parent == t->nil) {
        return;
      }

      if (parent == parent->parent->left) {
        delete_fixup(t, parent, 0);
      } else {
        delete_fixup(t, parent, 1);
      }    
      return;
    }  

    //케이스 2-4
    if (parent->color == RBTREE_BLACK && s->color == RBTREE_RED && l->color == RBTREE_BLACK && r->color == RBTREE_BLACK) { 
      printf("케이스 2-4 (왼)\n");
      left_rotate(t, parent);
      parent->color = !(parent->color);
      s->color = !(s->color);
      printf("^-^^%d\n",now->parent->key);
      printf("^-^^%p\n",now->parent->left);
      printf("^-^^%p\n",now);
      printf("^-^^%d\n",now->key);

      delete_fixup(t, now, dir);
      return;
    }
  } else {
    // 케이스 1-1
    if (parent->color == RBTREE_RED && s->color == RBTREE_BLACK && l->color == RBTREE_BLACK && r->color == RBTREE_BLACK) {
      printf("케이스 1-1 (오)\n");
      parent->color = !(parent->color);
      s->color = !(s->color);
      return;
    }

    if (s->color == RBTREE_BLACK) {
      // if (s->color == RBTREE_BLACK && l->color == RBTREE_RED && r->color == RBTREE_BLACK) {
      if (r->color == RBTREE_RED && l->color == RBTREE_BLACK) {
        printf("케이스 *-3 (오)\n");
        left_rotate(t, s);
        int tmp_color = l->color;
        l->color = s->color;
        s->color = tmp_color;
      } 
      
      if(l->color == RBTREE_RED) {
        printf("케이스 *-2 (오)\n"); 
        //p를 중심으로 왼쪽으로 회전
        right_rotate(t, parent);

        //p와 s의 색깔을 바꿈
        int tmp_color = parent->color;
        parent->color = s->color;
        s->color = tmp_color;

        //l을 레드에서 블랙으로
        l->color = !(l->color);
        return;
      } 
      
    }

    //케이스 2-1
    if (parent->color == RBTREE_BLACK && s->color == RBTREE_BLACK && r->color == RBTREE_BLACK && l->color == RBTREE_BLACK) { 
      printf("케이스 2-1 (오)\n");
      s->color = !(s->color);
      if (parent->parent == t->nil) {
        return;
      }
      if (parent == parent->parent->left) {
        delete_fixup(t, parent, 0);
      } else {
        delete_fixup(t, parent, 1);
      }    
      return;
    }  

    //케이스 2-4
    if (parent->color == RBTREE_BLACK && s->color == RBTREE_RED && r->color == RBTREE_BLACK && l->color == RBTREE_BLACK) { 
      printf("케이스 2-4 (오)\n");
      right_rotate(t, parent);
      parent->color = !(parent->color);
      s->color = !(s->color);
      
      delete_fixup(t, now, dir);
      return;
    }
  }
  return;
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
  if (now->parent != t->nil) {
    printf("부모는 %d   ", now->parent->key);
  }
  printf("\n");
  if (now->right != t->nil) {
    print_tree(t, now->right);
  }
}

// void test_find_erase(rbtree *t, const key_t *arr, const size_t n) {
//   for (int i = 0; i < n; i++) {
//     node_t *p = rbtree_insert(t, arr[i]);
//   }

//   for (int i = 0; i < n; i++) {
//     node_t *p = rbtree_find(t, arr[i]);
//     // printf("arr[%d] = %d\n", i, arr[i]);
//     // rbtree_erase(t, p);
//   }

// }

int main() {
  // int n = 16;
  // srand(17);
  rbtree *p = new_rbtree();
  // key_t *arr = calloc(n, sizeof(key_t));
  // for (int i = 0; i < n; i++) {
  //   arr[i] = rand();
  //   printf("%d\n",arr[i]);
  // }

  // test_find_erase(t, arr, n);

  // free(arr);
  // delete_rbtree(t);

  int num[] = {20,10,15,19};
	for (int i = 0; i <= 3; i++) {
		rbtree_insert(p, num[i]);
  }

  for (int i = 0; i <= 2; i++) {
    print_tree(p, p->root);
    node_t *now = rbtree_find(p, num[i]);
    printf("%d================\n", num[i]);
    rbtree_erase(p, now);
  }

  
  printf("%d\n", p->root->key);
  printf("%d\n", p->nil->key);
  print_tree(p, p->root);

  // printf("%p\n", p->root->left);
  // printf("%p\n", p->root->right);
  // printf("%p\n", p->root->parent);

  // printf("%d\n", p->root->parent==p->nil);

  // int num[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
	// for (int i = 0; i <= 9; i++) {
	// 	rbtree_insert(p, num[i]);
  // }

  // rbtree_erase(p, rbtree_find(p, 10));
  // rbtree_erase(p, rbtree_find(p, 5));
  // print_tree(p, p->root);
  // rbtree_erase(p, rbtree_find(p, 5));

}
