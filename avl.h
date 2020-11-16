#ifndef GRPC_CORE_LIB_AVL_AVL_H

#define GRPC_CORE_LIB_AVL_AVL_H
#include <grpc/support/port_platform.h>

#include <grpc/support/sync.h>

typedef struct grpc_avl_node {
	gpr_refcount refs;
	void* key;
	void* value;
	struct grpc_avl_node* left;
	struct grpc_avl_node* right;
	long height;
} grpc_avl_node;

typedef struct grpc_avl_vtable {
	void (*destroy_key)(void* key, void* user_data);
	void* (*copy_key)(void* key, void* user_data);
	long (*compare_keys)(void* key1, void* key2, void* user_data);
	void (*destroy_value)(void* value, void* user_data);
	void* (*copy_value)(void* value, void* user_data);
} grpc_avl_vtable;

typedef struct grpc_avl {
	const grpc_avl_vtable* vtable;
	grpc_avl_node* root;
} grpc_avl;

grpc_avl grpc_avl_create(const grpc_avl_vtable* vtable);

grpc_avl grpc_avl_ref(grpc_avl avl, void* user_data);

void grpc_avl_unref(grpc_avl avl, void* user_data);

grpc_avl grpc_avl_add(grpc_avl avl, void* key, void* value, void* user_data);

grpc_avl grpc_avl_remove(grpc_avl avl, void* key, void* value);

void* grpc_avl_get(grpc_avl avl, void* key, void* user_data);

int grpc_avl_maybe_get(grpc_avl avl, void* key, void** value, void* user_data);

int grpc_avl_is_empty(grpc_avl avl);

#endif