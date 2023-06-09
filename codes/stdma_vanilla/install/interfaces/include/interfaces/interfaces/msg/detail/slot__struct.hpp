// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/Slot.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__SLOT__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__SLOT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces__msg__Slot __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__Slot __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Slot_
{
  using Type = Slot_<ContainerAllocator>;

  explicit Slot_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->slot_no = 0;
      this->slot_total = 0;
      this->sender_no = 0;
      this->occupied = false;
    }
  }

  explicit Slot_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->slot_no = 0;
      this->slot_total = 0;
      this->sender_no = 0;
      this->occupied = false;
    }
  }

  // field types and members
  using _slot_no_type =
    int16_t;
  _slot_no_type slot_no;
  using _slot_total_type =
    int16_t;
  _slot_total_type slot_total;
  using _sender_no_type =
    int16_t;
  _sender_no_type sender_no;
  using _occupied_type =
    bool;
  _occupied_type occupied;

  // setters for named parameter idiom
  Type & set__slot_no(
    const int16_t & _arg)
  {
    this->slot_no = _arg;
    return *this;
  }
  Type & set__slot_total(
    const int16_t & _arg)
  {
    this->slot_total = _arg;
    return *this;
  }
  Type & set__sender_no(
    const int16_t & _arg)
  {
    this->sender_no = _arg;
    return *this;
  }
  Type & set__occupied(
    const bool & _arg)
  {
    this->occupied = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::Slot_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::Slot_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::Slot_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::Slot_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Slot_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Slot_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Slot_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Slot_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::Slot_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::Slot_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__Slot
    std::shared_ptr<interfaces::msg::Slot_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__Slot
    std::shared_ptr<interfaces::msg::Slot_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Slot_ & other) const
  {
    if (this->slot_no != other.slot_no) {
      return false;
    }
    if (this->slot_total != other.slot_total) {
      return false;
    }
    if (this->sender_no != other.sender_no) {
      return false;
    }
    if (this->occupied != other.occupied) {
      return false;
    }
    return true;
  }
  bool operator!=(const Slot_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Slot_

// alias to use template instance with default allocator
using Slot =
  interfaces::msg::Slot_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__SLOT__STRUCT_HPP_
