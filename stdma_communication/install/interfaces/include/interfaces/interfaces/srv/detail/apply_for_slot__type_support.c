// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interfaces:srv/ApplyForSlot.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interfaces/srv/detail/apply_for_slot__rosidl_typesupport_introspection_c.h"
#include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interfaces/srv/detail/apply_for_slot__functions.h"
#include "interfaces/srv/detail/apply_for_slot__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__srv__ApplyForSlot_Request__init(message_memory);
}

void interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_fini_function(void * message_memory)
{
  interfaces__srv__ApplyForSlot_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_message_member_array[2] = {
  {
    "applicant",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__srv__ApplyForSlot_Request, applicant),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "apply_slot",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__srv__ApplyForSlot_Request, apply_slot),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_message_members = {
  "interfaces__srv",  // message namespace
  "ApplyForSlot_Request",  // message name
  2,  // number of fields
  sizeof(interfaces__srv__ApplyForSlot_Request),
  interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_message_member_array,  // message members
  interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_message_type_support_handle = {
  0,
  &interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, ApplyForSlot_Request)() {
  if (!interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_message_type_support_handle.typesupport_identifier) {
    interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interfaces__srv__ApplyForSlot_Request__rosidl_typesupport_introspection_c__ApplyForSlot_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/srv/detail/apply_for_slot__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/srv/detail/apply_for_slot__functions.h"
// already included above
// #include "interfaces/srv/detail/apply_for_slot__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces__srv__ApplyForSlot_Response__init(message_memory);
}

void interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_fini_function(void * message_memory)
{
  interfaces__srv__ApplyForSlot_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_message_member_array[1] = {
  {
    "result",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__srv__ApplyForSlot_Response, result),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_message_members = {
  "interfaces__srv",  // message namespace
  "ApplyForSlot_Response",  // message name
  1,  // number of fields
  sizeof(interfaces__srv__ApplyForSlot_Response),
  interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_message_member_array,  // message members
  interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_message_type_support_handle = {
  0,
  &interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, ApplyForSlot_Response)() {
  if (!interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_message_type_support_handle.typesupport_identifier) {
    interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interfaces__srv__ApplyForSlot_Response__rosidl_typesupport_introspection_c__ApplyForSlot_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interfaces/srv/detail/apply_for_slot__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interfaces__srv__detail__apply_for_slot__rosidl_typesupport_introspection_c__ApplyForSlot_service_members = {
  "interfaces__srv",  // service namespace
  "ApplyForSlot",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // interfaces__srv__detail__apply_for_slot__rosidl_typesupport_introspection_c__ApplyForSlot_Request_message_type_support_handle,
  NULL  // response message
  // interfaces__srv__detail__apply_for_slot__rosidl_typesupport_introspection_c__ApplyForSlot_Response_message_type_support_handle
};

static rosidl_service_type_support_t interfaces__srv__detail__apply_for_slot__rosidl_typesupport_introspection_c__ApplyForSlot_service_type_support_handle = {
  0,
  &interfaces__srv__detail__apply_for_slot__rosidl_typesupport_introspection_c__ApplyForSlot_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, ApplyForSlot_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, ApplyForSlot_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, ApplyForSlot)() {
  if (!interfaces__srv__detail__apply_for_slot__rosidl_typesupport_introspection_c__ApplyForSlot_service_type_support_handle.typesupport_identifier) {
    interfaces__srv__detail__apply_for_slot__rosidl_typesupport_introspection_c__ApplyForSlot_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interfaces__srv__detail__apply_for_slot__rosidl_typesupport_introspection_c__ApplyForSlot_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, ApplyForSlot_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, ApplyForSlot_Response)()->data;
  }

  return &interfaces__srv__detail__apply_for_slot__rosidl_typesupport_introspection_c__ApplyForSlot_service_type_support_handle;
}
