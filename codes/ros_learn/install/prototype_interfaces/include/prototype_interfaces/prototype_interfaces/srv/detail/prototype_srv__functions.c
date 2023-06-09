// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from prototype_interfaces:srv/PrototypeSrv.idl
// generated code does not contain a copyright notice
#include "prototype_interfaces/srv/detail/prototype_srv__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"

bool
prototype_interfaces__srv__PrototypeSrv_Request__init(prototype_interfaces__srv__PrototypeSrv_Request * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    prototype_interfaces__srv__PrototypeSrv_Request__fini(msg);
    return false;
  }
  // borrow
  return true;
}

void
prototype_interfaces__srv__PrototypeSrv_Request__fini(prototype_interfaces__srv__PrototypeSrv_Request * msg)
{
  if (!msg) {
    return;
  }
  // name
  rosidl_runtime_c__String__fini(&msg->name);
  // borrow
}

bool
prototype_interfaces__srv__PrototypeSrv_Request__are_equal(const prototype_interfaces__srv__PrototypeSrv_Request * lhs, const prototype_interfaces__srv__PrototypeSrv_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // borrow
  if (lhs->borrow != rhs->borrow) {
    return false;
  }
  return true;
}

bool
prototype_interfaces__srv__PrototypeSrv_Request__copy(
  const prototype_interfaces__srv__PrototypeSrv_Request * input,
  prototype_interfaces__srv__PrototypeSrv_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // borrow
  output->borrow = input->borrow;
  return true;
}

prototype_interfaces__srv__PrototypeSrv_Request *
prototype_interfaces__srv__PrototypeSrv_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  prototype_interfaces__srv__PrototypeSrv_Request * msg = (prototype_interfaces__srv__PrototypeSrv_Request *)allocator.allocate(sizeof(prototype_interfaces__srv__PrototypeSrv_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(prototype_interfaces__srv__PrototypeSrv_Request));
  bool success = prototype_interfaces__srv__PrototypeSrv_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
prototype_interfaces__srv__PrototypeSrv_Request__destroy(prototype_interfaces__srv__PrototypeSrv_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    prototype_interfaces__srv__PrototypeSrv_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
prototype_interfaces__srv__PrototypeSrv_Request__Sequence__init(prototype_interfaces__srv__PrototypeSrv_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  prototype_interfaces__srv__PrototypeSrv_Request * data = NULL;

  if (size) {
    data = (prototype_interfaces__srv__PrototypeSrv_Request *)allocator.zero_allocate(size, sizeof(prototype_interfaces__srv__PrototypeSrv_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = prototype_interfaces__srv__PrototypeSrv_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        prototype_interfaces__srv__PrototypeSrv_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
prototype_interfaces__srv__PrototypeSrv_Request__Sequence__fini(prototype_interfaces__srv__PrototypeSrv_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      prototype_interfaces__srv__PrototypeSrv_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

prototype_interfaces__srv__PrototypeSrv_Request__Sequence *
prototype_interfaces__srv__PrototypeSrv_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  prototype_interfaces__srv__PrototypeSrv_Request__Sequence * array = (prototype_interfaces__srv__PrototypeSrv_Request__Sequence *)allocator.allocate(sizeof(prototype_interfaces__srv__PrototypeSrv_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = prototype_interfaces__srv__PrototypeSrv_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
prototype_interfaces__srv__PrototypeSrv_Request__Sequence__destroy(prototype_interfaces__srv__PrototypeSrv_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    prototype_interfaces__srv__PrototypeSrv_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
prototype_interfaces__srv__PrototypeSrv_Request__Sequence__are_equal(const prototype_interfaces__srv__PrototypeSrv_Request__Sequence * lhs, const prototype_interfaces__srv__PrototypeSrv_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!prototype_interfaces__srv__PrototypeSrv_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
prototype_interfaces__srv__PrototypeSrv_Request__Sequence__copy(
  const prototype_interfaces__srv__PrototypeSrv_Request__Sequence * input,
  prototype_interfaces__srv__PrototypeSrv_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(prototype_interfaces__srv__PrototypeSrv_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    prototype_interfaces__srv__PrototypeSrv_Request * data =
      (prototype_interfaces__srv__PrototypeSrv_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!prototype_interfaces__srv__PrototypeSrv_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          prototype_interfaces__srv__PrototypeSrv_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!prototype_interfaces__srv__PrototypeSrv_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
prototype_interfaces__srv__PrototypeSrv_Response__init(prototype_interfaces__srv__PrototypeSrv_Response * msg)
{
  if (!msg) {
    return false;
  }
  // lend_or_not
  // lend
  return true;
}

void
prototype_interfaces__srv__PrototypeSrv_Response__fini(prototype_interfaces__srv__PrototypeSrv_Response * msg)
{
  if (!msg) {
    return;
  }
  // lend_or_not
  // lend
}

bool
prototype_interfaces__srv__PrototypeSrv_Response__are_equal(const prototype_interfaces__srv__PrototypeSrv_Response * lhs, const prototype_interfaces__srv__PrototypeSrv_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // lend_or_not
  if (lhs->lend_or_not != rhs->lend_or_not) {
    return false;
  }
  // lend
  if (lhs->lend != rhs->lend) {
    return false;
  }
  return true;
}

bool
prototype_interfaces__srv__PrototypeSrv_Response__copy(
  const prototype_interfaces__srv__PrototypeSrv_Response * input,
  prototype_interfaces__srv__PrototypeSrv_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // lend_or_not
  output->lend_or_not = input->lend_or_not;
  // lend
  output->lend = input->lend;
  return true;
}

prototype_interfaces__srv__PrototypeSrv_Response *
prototype_interfaces__srv__PrototypeSrv_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  prototype_interfaces__srv__PrototypeSrv_Response * msg = (prototype_interfaces__srv__PrototypeSrv_Response *)allocator.allocate(sizeof(prototype_interfaces__srv__PrototypeSrv_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(prototype_interfaces__srv__PrototypeSrv_Response));
  bool success = prototype_interfaces__srv__PrototypeSrv_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
prototype_interfaces__srv__PrototypeSrv_Response__destroy(prototype_interfaces__srv__PrototypeSrv_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    prototype_interfaces__srv__PrototypeSrv_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
prototype_interfaces__srv__PrototypeSrv_Response__Sequence__init(prototype_interfaces__srv__PrototypeSrv_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  prototype_interfaces__srv__PrototypeSrv_Response * data = NULL;

  if (size) {
    data = (prototype_interfaces__srv__PrototypeSrv_Response *)allocator.zero_allocate(size, sizeof(prototype_interfaces__srv__PrototypeSrv_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = prototype_interfaces__srv__PrototypeSrv_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        prototype_interfaces__srv__PrototypeSrv_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
prototype_interfaces__srv__PrototypeSrv_Response__Sequence__fini(prototype_interfaces__srv__PrototypeSrv_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      prototype_interfaces__srv__PrototypeSrv_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

prototype_interfaces__srv__PrototypeSrv_Response__Sequence *
prototype_interfaces__srv__PrototypeSrv_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  prototype_interfaces__srv__PrototypeSrv_Response__Sequence * array = (prototype_interfaces__srv__PrototypeSrv_Response__Sequence *)allocator.allocate(sizeof(prototype_interfaces__srv__PrototypeSrv_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = prototype_interfaces__srv__PrototypeSrv_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
prototype_interfaces__srv__PrototypeSrv_Response__Sequence__destroy(prototype_interfaces__srv__PrototypeSrv_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    prototype_interfaces__srv__PrototypeSrv_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
prototype_interfaces__srv__PrototypeSrv_Response__Sequence__are_equal(const prototype_interfaces__srv__PrototypeSrv_Response__Sequence * lhs, const prototype_interfaces__srv__PrototypeSrv_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!prototype_interfaces__srv__PrototypeSrv_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
prototype_interfaces__srv__PrototypeSrv_Response__Sequence__copy(
  const prototype_interfaces__srv__PrototypeSrv_Response__Sequence * input,
  prototype_interfaces__srv__PrototypeSrv_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(prototype_interfaces__srv__PrototypeSrv_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    prototype_interfaces__srv__PrototypeSrv_Response * data =
      (prototype_interfaces__srv__PrototypeSrv_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!prototype_interfaces__srv__PrototypeSrv_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          prototype_interfaces__srv__PrototypeSrv_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!prototype_interfaces__srv__PrototypeSrv_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
