// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/MapSending.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MAP_SENDING__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__MAP_SENDING__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__MapSending_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__MapSending_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MapSending_Request_
{
  using Type = MapSending_Request_<ContainerAllocator>;

  explicit MapSending_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->applicant = 0;
    }
  }

  explicit MapSending_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->applicant = 0;
    }
  }

  // field types and members
  using _applicant_type =
    int16_t;
  _applicant_type applicant;

  // setters for named parameter idiom
  Type & set__applicant(
    const int16_t & _arg)
  {
    this->applicant = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::MapSending_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::MapSending_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::MapSending_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::MapSending_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MapSending_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MapSending_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MapSending_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MapSending_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::MapSending_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::MapSending_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__MapSending_Request
    std::shared_ptr<interfaces::srv::MapSending_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__MapSending_Request
    std::shared_ptr<interfaces::srv::MapSending_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MapSending_Request_ & other) const
  {
    if (this->applicant != other.applicant) {
      return false;
    }
    return true;
  }
  bool operator!=(const MapSending_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MapSending_Request_

// alias to use template instance with default allocator
using MapSending_Request =
  interfaces::srv::MapSending_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__MapSending_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__MapSending_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MapSending_Response_
{
  using Type = MapSending_Response_<ContainerAllocator>;

  explicit MapSending_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit MapSending_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _map_data_type =
    std::vector<int16_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int16_t>>;
  _map_data_type map_data;

  // setters for named parameter idiom
  Type & set__map_data(
    const std::vector<int16_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int16_t>> & _arg)
  {
    this->map_data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::MapSending_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::MapSending_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::MapSending_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::MapSending_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MapSending_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MapSending_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MapSending_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MapSending_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::MapSending_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::MapSending_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__MapSending_Response
    std::shared_ptr<interfaces::srv::MapSending_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__MapSending_Response
    std::shared_ptr<interfaces::srv::MapSending_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MapSending_Response_ & other) const
  {
    if (this->map_data != other.map_data) {
      return false;
    }
    return true;
  }
  bool operator!=(const MapSending_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MapSending_Response_

// alias to use template instance with default allocator
using MapSending_Response =
  interfaces::srv::MapSending_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct MapSending
{
  using Request = interfaces::srv::MapSending_Request;
  using Response = interfaces::srv::MapSending_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__MAP_SENDING__STRUCT_HPP_
