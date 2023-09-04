#include "rbtree.h"

#include <stdio.h>
#include <stdlib.h>

node_t *get_new_node(rbtree *tree, key_t key);
void rotate_left(rbtree *tree, node_t *node_x);
void rotate_right(rbtree *tree, node_t *node_y);
void show_tree(rbtree *tree, node_t *node);
void rebuild_after_insert(rbtree *tree, node_t *new_node);
void show_single_node(node_t *node);

rbtree *new_rbtree(void) {
    rbtree *tree = (rbtree *) malloc(sizeof(rbtree));
    node_t *nil = (node_t *) malloc(sizeof(node_t));

    nil -> color = RBTREE_BLACK;
    tree -> nil = tree -> root = nil;

    return tree;
}

void delete_rbtree(rbtree *t) {
   free(t);
}

// 새로운 노드는 red를 갖는다

// 1. 루트 노를 시작으로 key 값을 비교해 left, right 타고 내려가서 insert 할 위치를 찾는다.
// 2. 1번 과정을 진행 하면서 다른 포인터 변수에 현재 찾으면서 내려가는 주소 한 칸 뒤를 저장한다. (1번과 같이 진행)
// (새로 insert 할 노드 자리를 기억해야하기 때문에)
// 3 - 1. 1, 2번 과정을 끝냈는데 뒤 따라가던 포인터변수가 NULL(NIL) 이라면 비어있는 트리이기 때문에 루트에 삽입한다.
// 3 - 2. key 값에 따라서 뒤 따라오던 포인터 변수의 left, right 어디에 삽입할지 결정한다.
// (새로 삽입된 노드는 리프노드가 되기 때문에 자식 노드는 자연스럽게 NIL 노드를 갖는다.)
// 4. RB Insert-Fixup 실행

// 1. 루트 노드는 black 이여야 한다.
// 2. red-red 위반 사항에 대해서 신경 써야한다.
node_t *rbtree_insert(rbtree *t, const key_t key) {
    node_t *new_node = get_new_node(t, key);
    node_t *insert_point = t -> nil;
    node_t *cur_node = t -> root;

    while(cur_node != t -> nil){
        insert_point = cur_node;
    
       if(key < cur_node -> key){
           cur_node = cur_node -> left;
       } else {
           cur_node = cur_node -> right;
       }
    }

    new_node -> parent = insert_point;

    if(insert_point == t -> nil){
       t -> root = new_node;
    } else if(key < insert_point -> key){
       insert_point -> left = new_node;
    } else {
       insert_point -> right = new_node;
    }

    rebuild_after_insert(t, new_node);
    return t -> root;
}

node_t *rbtree_find(const rbtree *t, const key_t key) {
    node_t *cur_node = t -> root;

    while(cur_node != t -> nil){
        if(key == cur_node -> key){
            break;
        }

        cur_node = key > cur_node -> key ? cur_node -> right : cur_node -> left;
    }

    if(cur_node == t -> nil){
        return NULL;
    }

    return t -> root;
}

node_t *rbtree_min(const rbtree *t) {
    node_t *cur_node = t -> root;

    while(cur_node -> left != t -> nil){
        cur_node = cur_node -> left;
    }

    printf("최소 값: %d\n", cur_node -> key);

    return cur_node;
    // return t -> root;
}

node_t *rbtree_max(const rbtree *t) {
    node_t *cur_node = t -> root;

    while(cur_node -> right != t -> nil){
        cur_node = cur_node -> right;
    }

    printf("최대 값: %d\n", cur_node -> key);

    return cur_node;
    //return t -> root;
}

int rbtree_erase(rbtree *t, node_t *p) {
    return 0;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
    return 0;
}

node_t *get_new_node(rbtree *tree, key_t key){
    node_t *new_node = (node_t *) malloc(sizeof(node_t));

    new_node -> left = new_node -> right = new_node -> parent = tree -> nil;
    new_node -> color = RBTREE_RED;
    new_node -> key = key;

    return new_node;
}

// (A4 용지 그림보고 할 것)
// 1. y 노드를 기억한다.
// 2. x의 오른쪽 자식은 '베타'가 된다. (x-y 연결을 끊는 개념)
// 3. y의 왼쪽 자식('베타')의 부모를 x로 한고, x의 오른쪽 자식은 y의 왼쪽 자식('베타')가 된다.
// 4 - 1. x의 부모를 y로 두고, x의 부모노드가 y의 부모노드가 된다.
// (x의 부모가 NIL 이라면(=root), y가 트리의 새로운 root가 된다.)
// 4 - 2. x가 부모의 왼쪽이면 y가 왼쪽, 오른쪽이면 오른쪽이 된다.
// 5. x가 y의 왼쪽 자식이 되고, y가 x의 부모가 된다.
// [ x의 부모, y의 부모, x의 오른쪽 자식, y의 왼쪽 자식, 부모의 자식 부분 ] ===> 주소 값 변경이 필요함
void rotate_left(rbtree *tree, node_t *node_x){
    node_t *node_y = node_x -> right;
    node_x -> right = node_y -> left;
    node_y -> left -> parent = node_x;
    node_y -> parent = node_x -> parent;

    if(node_x -> parent == tree -> nil){
        tree -> root = node_y;
    } else if(node_x == node_x -> parent -> left){
        node_y -> parent -> left = node_y;
    } else {
        node_y -> parent -> right = node_y;
    }

    node_y -> left = node_x;
    node_x -> parent = node_y;
}

void rotate_right(rbtree *tree, node_t *node_y){
    node_t *node_x = node_y -> left;
    node_y -> left = node_x -> right;
    node_x -> right -> parent = node_y;
    node_x -> parent = node_y -> parent;

    if(node_y -> parent == tree -> nil){
        tree -> root = node_x;
    } else if(node_y == node_y -> parent -> left){
        node_x -> parent -> left = node_x;
    } else {
        node_x -> parent -> right = node_x;
    }

    node_x -> right = node_y;
    node_y -> parent = node_x;
}

void rebuild_after_insert(rbtree *tree, node_t *node_z){
    node_t *node_y = tree -> nil;

    while(node_z -> parent -> color == RBTREE_RED){
        if(node_z -> parent == node_z -> parent -> parent -> left){
            node_y = node_z -> parent -> parent -> right;

            if(node_y -> color == RBTREE_RED){
                node_z -> parent -> color = RBTREE_BLACK;
                node_y -> color = RBTREE_BLACK;
                node_z -> parent -> parent -> color = RBTREE_RED;

                node_z = node_z -> parent -> parent;
            } else {
                if(node_z == node_z -> parent -> right){
                    node_z = node_z -> parent;
                    rotate_left(tree, node_z);
                }

                node_z -> parent -> color = RBTREE_BLACK;
                node_z -> parent -> parent -> color = RBTREE_RED;

                rotate_right(tree, node_z -> parent -> parent);
            }
        } else {
            node_y = node_z -> parent -> parent -> left;

            if(node_y -> color == RBTREE_RED){
                node_z -> parent -> color = RBTREE_BLACK;
                node_y -> color = RBTREE_BLACK;
                node_z -> parent -> parent -> color = RBTREE_RED;

                node_z = node_z -> parent -> parent;
            } else {
                if(node_z == node_z -> parent -> left){
                    node_z = node_z -> parent;
                    rotate_right(tree, node_z);
                }

                node_z -> parent -> color = RBTREE_BLACK;
                node_z -> parent -> parent -> color = RBTREE_RED;
                
                rotate_left(tree, node_z -> parent -> parent);
            }
        }
    }

    tree -> root -> color = RBTREE_BLACK;
}

void show_single_node(node_t *node){
    printf("(key = %d", node -> key);
    printf("    color = %s)\n", node -> color == 0 ? "R" : "B");
}

void show_tree(rbtree *tree, node_t *node){
    if(node == tree -> nil){
        return;
    }

    if(node -> left != tree -> nil){
        show_tree(tree, node -> left);
    }

    printf("%d, %s\n", node -> key, node -> color == 0 ? "RED" : "BLACK");

    if(node -> right != tree -> nil){
        show_tree(tree, node -> right);
    }
}
