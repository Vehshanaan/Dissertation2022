// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/ApplyForSlot.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__ApplyForSlot_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__ApplyForSlot_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ApplyForSlot_Request_
{
  using Type = ApplyForSlot_Request_<ContainerAllocator>;

  explicit ApplyForSlot_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->applicant = 0;
      this->apply_slot = 0;
    }
  }

  explicit ApplyForSlot_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->applicant = 0;
      this->apply_slot = 0;
    }
  }

  // field types and members
  using _applicant_type =
    int16_t;
  _applicant_type applicant;
  using _apply_slot_type =
    int16_t;
  _apply_slot_type apply_slot;

  // setters for named parameter idiom
  Type & set__applicant(
    const int16_t & _arg)
  {
    this->applicant = _arg;
    return *this;
  }
  Type & set__apply_slot(
    const int16_t & _arg)
  {
    this->apply_slot = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::ApplyForSlot_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::ApplyForSlot_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::ApplyForSlot_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::ApplyForSlot_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::ApplyForSlot_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::ApplyForSlot_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::ApplyForSlot_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::ApplyForSlot_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::ApplyForSlot_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::ApplyForSlot_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__ApplyForSlot_Request
    std::shared_ptr<interfaces::srv::ApplyForSlot_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__ApplyForSlot_Request
    std::shared_ptr<interfaces::srv::ApplyForSlot_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ApplyForSlot_Request_ & other) const
  {
    if (this->applicant != other.applicant) {
      return false;
    }
    if (this->apply_slot != other.apply_slot) {
      return false;
    }
    return true;
  }
  bool operator!=(const ApplyForSlot_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ApplyForSlot_Request_

// alias to use template instance with default allocator
using ApplyForSlot_Request =
  interfaces::srv::ApplyForSlot_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__ApplyForSlot_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__ApplyForSlot_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ApplyForSlot_Response_
{
  using Type = ApplyForSlot_Response_<ContainerAllocator>;

  explicit ApplyForSlot_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  explicit ApplyForSlot_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  // field types and members
  using _result_type =
    bool;
  _result_type result;

  // setters for named parameter idiom
  Type & set__result(
    const bool & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::ApplyForSlot_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::ApplyForSlot_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::ApplyForSlot_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::ApplyForSlot_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::ApplyForSlot_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::ApplyForSlot_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::ApplyForSlot_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::ApplyForSlot_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::ApplyForSlot_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::ApplyForSlot_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__ApplyForSlot_Response
    std::shared_ptr<interfaces::srv::ApplyForSlot_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__ApplyForSlot_Response
    std::shared_ptr<interfaces::srv::ApplyForSlot_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ApplyForSlot_Response_ & other) const
  {
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const ApplyForSlot_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ApplyForSlot_Response_

// alias to use template instance with default allocator
using ApplyForSlot_Response =
  interfaces::srv::ApplyForSlot_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct ApplyForSlot
{
  using Request = interfaces::srv::ApplyForSlot_Request;
  using Response = interfaces::srv::ApplyForSlot_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__STRUCT_HPP_
