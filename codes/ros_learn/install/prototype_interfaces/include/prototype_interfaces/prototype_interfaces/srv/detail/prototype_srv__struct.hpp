// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from prototype_interfaces:srv/PrototypeSrv.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__STRUCT_HPP_
#define PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__prototype_interfaces__srv__PrototypeSrv_Request __attribute__((deprecated))
#else
# define DEPRECATED__prototype_interfaces__srv__PrototypeSrv_Request __declspec(deprecated)
#endif

namespace prototype_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct PrototypeSrv_Request_
{
  using Type = PrototypeSrv_Request_<ContainerAllocator>;

  explicit PrototypeSrv_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->name = "";
      this->borrow = 0l;
    }
  }

  explicit PrototypeSrv_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->name = "";
      this->borrow = 0l;
    }
  }

  // field types and members
  using _name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _name_type name;
  using _borrow_type =
    int32_t;
  _borrow_type borrow;

  // setters for named parameter idiom
  Type & set__name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->name = _arg;
    return *this;
  }
  Type & set__borrow(
    const int32_t & _arg)
  {
    this->borrow = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__prototype_interfaces__srv__PrototypeSrv_Request
    std::shared_ptr<prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__prototype_interfaces__srv__PrototypeSrv_Request
    std::shared_ptr<prototype_interfaces::srv::PrototypeSrv_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PrototypeSrv_Request_ & other) const
  {
    if (this->name != other.name) {
      return false;
    }
    if (this->borrow != other.borrow) {
      return false;
    }
    return true;
  }
  bool operator!=(const PrototypeSrv_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PrototypeSrv_Request_

// alias to use template instance with default allocator
using PrototypeSrv_Request =
  prototype_interfaces::srv::PrototypeSrv_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace prototype_interfaces


#ifndef _WIN32
# define DEPRECATED__prototype_interfaces__srv__PrototypeSrv_Response __attribute__((deprecated))
#else
# define DEPRECATED__prototype_interfaces__srv__PrototypeSrv_Response __declspec(deprecated)
#endif

namespace prototype_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct PrototypeSrv_Response_
{
  using Type = PrototypeSrv_Response_<ContainerAllocator>;

  explicit PrototypeSrv_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->lend_or_not = false;
      this->lend = 0l;
    }
  }

  explicit PrototypeSrv_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->lend_or_not = false;
      this->lend = 0l;
    }
  }

  // field types and members
  using _lend_or_not_type =
    bool;
  _lend_or_not_type lend_or_not;
  using _lend_type =
    int32_t;
  _lend_type lend;

  // setters for named parameter idiom
  Type & set__lend_or_not(
    const bool & _arg)
  {
    this->lend_or_not = _arg;
    return *this;
  }
  Type & set__lend(
    const int32_t & _arg)
  {
    this->lend = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__prototype_interfaces__srv__PrototypeSrv_Response
    std::shared_ptr<prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__prototype_interfaces__srv__PrototypeSrv_Response
    std::shared_ptr<prototype_interfaces::srv::PrototypeSrv_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PrototypeSrv_Response_ & other) const
  {
    if (this->lend_or_not != other.lend_or_not) {
      return false;
    }
    if (this->lend != other.lend) {
      return false;
    }
    return true;
  }
  bool operator!=(const PrototypeSrv_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PrototypeSrv_Response_

// alias to use template instance with default allocator
using PrototypeSrv_Response =
  prototype_interfaces::srv::PrototypeSrv_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace prototype_interfaces

namespace prototype_interfaces
{

namespace srv
{

struct PrototypeSrv
{
  using Request = prototype_interfaces::srv::PrototypeSrv_Request;
  using Response = prototype_interfaces::srv::PrototypeSrv_Response;
};

}  // namespace srv

}  // namespace prototype_interfaces

#endif  // PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__STRUCT_HPP_
