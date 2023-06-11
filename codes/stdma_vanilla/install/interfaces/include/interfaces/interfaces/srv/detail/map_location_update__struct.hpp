// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/MapLocationUpdate.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__MapLocationUpdate_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__MapLocationUpdate_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MapLocationUpdate_Request_
{
  using Type = MapLocationUpdate_Request_<ContainerAllocator>;

  explicit MapLocationUpdate_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->applicant = 0;
      this->x = 0;
      this->y = 0;
    }
  }

  explicit MapLocationUpdate_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->applicant = 0;
      this->x = 0;
      this->y = 0;
    }
  }

  // field types and members
  using _applicant_type =
    int16_t;
  _applicant_type applicant;
  using _x_type =
    int16_t;
  _x_type x;
  using _y_type =
    int16_t;
  _y_type y;

  // setters for named parameter idiom
  Type & set__applicant(
    const int16_t & _arg)
  {
    this->applicant = _arg;
    return *this;
  }
  Type & set__x(
    const int16_t & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const int16_t & _arg)
  {
    this->y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__MapLocationUpdate_Request
    std::shared_ptr<interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__MapLocationUpdate_Request
    std::shared_ptr<interfaces::srv::MapLocationUpdate_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MapLocationUpdate_Request_ & other) const
  {
    if (this->applicant != other.applicant) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    return true;
  }
  bool operator!=(const MapLocationUpdate_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MapLocationUpdate_Request_

// alias to use template instance with default allocator
using MapLocationUpdate_Request =
  interfaces::srv::MapLocationUpdate_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__MapLocationUpdate_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__MapLocationUpdate_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MapLocationUpdate_Response_
{
  using Type = MapLocationUpdate_Response_<ContainerAllocator>;

  explicit MapLocationUpdate_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit MapLocationUpdate_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__MapLocationUpdate_Response
    std::shared_ptr<interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__MapLocationUpdate_Response
    std::shared_ptr<interfaces::srv::MapLocationUpdate_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MapLocationUpdate_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const MapLocationUpdate_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MapLocationUpdate_Response_

// alias to use template instance with default allocator
using MapLocationUpdate_Response =
  interfaces::srv::MapLocationUpdate_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct MapLocationUpdate
{
  using Request = interfaces::srv::MapLocationUpdate_Request;
  using Response = interfaces::srv::MapLocationUpdate_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__STRUCT_HPP_
