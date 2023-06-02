// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:msg/Slot.idl
// generated code does not contain a copyright notice
#include "interfaces/msg/detail/slot__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
interfaces__msg__Slot__init(interfaces__msg__Slot * msg)
{
  if (!msg) {
    return false;
  }
  // slot_no
  // slot_total
  // sender_no
  // occupied
  return true;
}

void
interfaces__msg__Slot__fini(interfaces__msg__Slot * msg)
{
  if (!msg) {
    return;
  }
  // slot_no
  // slot_total
  // sender_no
  // occupied
}

bool
interfaces__msg__Slot__are_equal(const interfaces__msg__Slot * lhs, const interfaces__msg__Slot * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // slot_no
  if (lhs->slot_no != rhs->slot_no) {
    return false;
  }
  // slot_total
  if (lhs->slot_total != rhs->slot_total) {
    return false;
  }
  // sender_no
  if (lhs->sender_no != rhs->sender_no) {
    return false;
  }
  // occupied
  if (lhs->occupied != rhs->occupied) {
    return false;
  }
  return true;
}

bool
interfaces__msg__Slot__copy(
  const interfaces__msg__Slot * input,
  interfaces__msg__Slot * output)
{
  if (!input || !output) {
    return false;
  }
  // slot_no
  output->slot_no = input->slot_no;
  // slot_total
  output->slot_total = input->slot_total;
  // sender_no
  output->sender_no = input->sender_no;
  // occupied
  output->occupied = input->occupied;
  return true;
}

interfaces__msg__Slot *
interfaces__msg__Slot__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__msg__Slot * msg = (interfaces__msg__Slot *)allocator.allocate(sizeof(interfaces__msg__Slot), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__msg__Slot));
  bool success = interfaces__msg__Slot__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interfaces__msg__Slot__destroy(interfaces__msg__Slot * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interfaces__msg__Slot__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interfaces__msg__Slot__Sequence__init(interfaces__msg__Slot__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__msg__Slot * data = NULL;

  if (size) {
    data = (interfaces__msg__Slot *)allocator.zero_allocate(size, sizeof(interfaces__msg__Slot), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__msg__Slot__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__msg__Slot__fini(&data[i - 1]);
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
interfaces__msg__Slot__Sequence__fini(interfaces__msg__Slot__Sequence * array)
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
      interfaces__msg__Slot__fini(&array->data[i]);
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

interfaces__msg__Slot__Sequence *
interfaces__msg__Slot__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__msg__Slot__Sequence * array = (interfaces__msg__Slot__Sequence *)allocator.allocate(sizeof(interfaces__msg__Slot__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interfaces__msg__Slot__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interfaces__msg__Slot__Sequence__destroy(interfaces__msg__Slot__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interfaces__msg__Slot__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interfaces__msg__Slot__Sequence__are_equal(const interfaces__msg__Slot__Sequence * lhs, const interfaces__msg__Slot__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__msg__Slot__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__msg__Slot__Sequence__copy(
  const interfaces__msg__Slot__Sequence * input,
  interfaces__msg__Slot__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__msg__Slot);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    interfaces__msg__Slot * data =
      (interfaces__msg__Slot *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__msg__Slot__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          interfaces__msg__Slot__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__msg__Slot__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
