// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from prototype_interfaces:msg/Prototype.idl
// generated code does not contain a copyright notice
#include "prototype_interfaces/msg/detail/prototype__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `content`
#include "std_msgs/msg/detail/string__functions.h"
// Member `image`
#include "sensor_msgs/msg/detail/image__functions.h"

bool
prototype_interfaces__msg__Prototype__init(prototype_interfaces__msg__Prototype * msg)
{
  if (!msg) {
    return false;
  }
  // content
  if (!std_msgs__msg__String__init(&msg->content)) {
    prototype_interfaces__msg__Prototype__fini(msg);
    return false;
  }
  // image
  if (!sensor_msgs__msg__Image__init(&msg->image)) {
    prototype_interfaces__msg__Prototype__fini(msg);
    return false;
  }
  return true;
}

void
prototype_interfaces__msg__Prototype__fini(prototype_interfaces__msg__Prototype * msg)
{
  if (!msg) {
    return;
  }
  // content
  std_msgs__msg__String__fini(&msg->content);
  // image
  sensor_msgs__msg__Image__fini(&msg->image);
}

bool
prototype_interfaces__msg__Prototype__are_equal(const prototype_interfaces__msg__Prototype * lhs, const prototype_interfaces__msg__Prototype * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // content
  if (!std_msgs__msg__String__are_equal(
      &(lhs->content), &(rhs->content)))
  {
    return false;
  }
  // image
  if (!sensor_msgs__msg__Image__are_equal(
      &(lhs->image), &(rhs->image)))
  {
    return false;
  }
  return true;
}

bool
prototype_interfaces__msg__Prototype__copy(
  const prototype_interfaces__msg__Prototype * input,
  prototype_interfaces__msg__Prototype * output)
{
  if (!input || !output) {
    return false;
  }
  // content
  if (!std_msgs__msg__String__copy(
      &(input->content), &(output->content)))
  {
    return false;
  }
  // image
  if (!sensor_msgs__msg__Image__copy(
      &(input->image), &(output->image)))
  {
    return false;
  }
  return true;
}

prototype_interfaces__msg__Prototype *
prototype_interfaces__msg__Prototype__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  prototype_interfaces__msg__Prototype * msg = (prototype_interfaces__msg__Prototype *)allocator.allocate(sizeof(prototype_interfaces__msg__Prototype), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(prototype_interfaces__msg__Prototype));
  bool success = prototype_interfaces__msg__Prototype__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
prototype_interfaces__msg__Prototype__destroy(prototype_interfaces__msg__Prototype * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    prototype_interfaces__msg__Prototype__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
prototype_interfaces__msg__Prototype__Sequence__init(prototype_interfaces__msg__Prototype__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  prototype_interfaces__msg__Prototype * data = NULL;

  if (size) {
    data = (prototype_interfaces__msg__Prototype *)allocator.zero_allocate(size, sizeof(prototype_interfaces__msg__Prototype), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = prototype_interfaces__msg__Prototype__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        prototype_interfaces__msg__Prototype__fini(&data[i - 1]);
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
prototype_interfaces__msg__Prototype__Sequence__fini(prototype_interfaces__msg__Prototype__Sequence * array)
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
      prototype_interfaces__msg__Prototype__fini(&array->data[i]);
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

prototype_interfaces__msg__Prototype__Sequence *
prototype_interfaces__msg__Prototype__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  prototype_interfaces__msg__Prototype__Sequence * array = (prototype_interfaces__msg__Prototype__Sequence *)allocator.allocate(sizeof(prototype_interfaces__msg__Prototype__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = prototype_interfaces__msg__Prototype__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
prototype_interfaces__msg__Prototype__Sequence__destroy(prototype_interfaces__msg__Prototype__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    prototype_interfaces__msg__Prototype__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
prototype_interfaces__msg__Prototype__Sequence__are_equal(const prototype_interfaces__msg__Prototype__Sequence * lhs, const prototype_interfaces__msg__Prototype__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!prototype_interfaces__msg__Prototype__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
prototype_interfaces__msg__Prototype__Sequence__copy(
  const prototype_interfaces__msg__Prototype__Sequence * input,
  prototype_interfaces__msg__Prototype__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(prototype_interfaces__msg__Prototype);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    prototype_interfaces__msg__Prototype * data =
      (prototype_interfaces__msg__Prototype *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!prototype_interfaces__msg__Prototype__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          prototype_interfaces__msg__Prototype__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!prototype_interfaces__msg__Prototype__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
