// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from prototype_interfaces:srv/PrototypeSrv.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "prototype_interfaces/srv/detail/prototype_srv__rosidl_typesupport_introspection_c.h"
#include "prototype_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "prototype_interfaces/srv/detail/prototype_srv__functions.h"
#include "prototype_interfaces/srv/detail/prototype_srv__struct.h"


// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  prototype_interfaces__srv__PrototypeSrv_Request__init(message_memory);
}

void prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_fini_function(void * message_memory)
{
  prototype_interfaces__srv__PrototypeSrv_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_message_member_array[2] = {
  {
    "name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(prototype_interfaces__srv__PrototypeSrv_Request, name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "borrow",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(prototype_interfaces__srv__PrototypeSrv_Request, borrow),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_message_members = {
  "prototype_interfaces__srv",  // message namespace
  "PrototypeSrv_Request",  // message name
  2,  // number of fields
  sizeof(prototype_interfaces__srv__PrototypeSrv_Request),
  prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_message_member_array,  // message members
  prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_message_type_support_handle = {
  0,
  &prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_prototype_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, prototype_interfaces, srv, PrototypeSrv_Request)() {
  if (!prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_message_type_support_handle.typesupport_identifier) {
    prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &prototype_interfaces__srv__PrototypeSrv_Request__rosidl_typesupport_introspection_c__PrototypeSrv_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "prototype_interfaces/srv/detail/prototype_srv__rosidl_typesupport_introspection_c.h"
// already included above
// #include "prototype_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "prototype_interfaces/srv/detail/prototype_srv__functions.h"
// already included above
// #include "prototype_interfaces/srv/detail/prototype_srv__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  prototype_interfaces__srv__PrototypeSrv_Response__init(message_memory);
}

void prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_fini_function(void * message_memory)
{
  prototype_interfaces__srv__PrototypeSrv_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_message_member_array[2] = {
  {
    "lend_or_not",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(prototype_interfaces__srv__PrototypeSrv_Response, lend_or_not),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "lend",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(prototype_interfaces__srv__PrototypeSrv_Response, lend),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_message_members = {
  "prototype_interfaces__srv",  // message namespace
  "PrototypeSrv_Response",  // message name
  2,  // number of fields
  sizeof(prototype_interfaces__srv__PrototypeSrv_Response),
  prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_message_member_array,  // message members
  prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_message_type_support_handle = {
  0,
  &prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_prototype_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, prototype_interfaces, srv, PrototypeSrv_Response)() {
  if (!prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_message_type_support_handle.typesupport_identifier) {
    prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &prototype_interfaces__srv__PrototypeSrv_Response__rosidl_typesupport_introspection_c__PrototypeSrv_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "prototype_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "prototype_interfaces/srv/detail/prototype_srv__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers prototype_interfaces__srv__detail__prototype_srv__rosidl_typesupport_introspection_c__PrototypeSrv_service_members = {
  "prototype_interfaces__srv",  // service namespace
  "PrototypeSrv",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // prototype_interfaces__srv__detail__prototype_srv__rosidl_typesupport_introspection_c__PrototypeSrv_Request_message_type_support_handle,
  NULL  // response message
  // prototype_interfaces__srv__detail__prototype_srv__rosidl_typesupport_introspection_c__PrototypeSrv_Response_message_type_support_handle
};

static rosidl_service_type_support_t prototype_interfaces__srv__detail__prototype_srv__rosidl_typesupport_introspection_c__PrototypeSrv_service_type_support_handle = {
  0,
  &prototype_interfaces__srv__detail__prototype_srv__rosidl_typesupport_introspection_c__PrototypeSrv_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, prototype_interfaces, srv, PrototypeSrv_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, prototype_interfaces, srv, PrototypeSrv_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_prototype_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, prototype_interfaces, srv, PrototypeSrv)() {
  if (!prototype_interfaces__srv__detail__prototype_srv__rosidl_typesupport_introspection_c__PrototypeSrv_service_type_support_handle.typesupport_identifier) {
    prototype_interfaces__srv__detail__prototype_srv__rosidl_typesupport_introspection_c__PrototypeSrv_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)prototype_interfaces__srv__detail__prototype_srv__rosidl_typesupport_introspection_c__PrototypeSrv_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, prototype_interfaces, srv, PrototypeSrv_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, prototype_interfaces, srv, PrototypeSrv_Response)()->data;
  }

  return &prototype_interfaces__srv__detail__prototype_srv__rosidl_typesupport_introspection_c__PrototypeSrv_service_type_support_handle;
}
