// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from prototype_interfaces:msg/Prototype.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__STRUCT_HPP_
#define PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'content'
#include "std_msgs/msg/detail/string__struct.hpp"
// Member 'image'
#include "sensor_msgs/msg/detail/image__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__prototype_interfaces__msg__Prototype __attribute__((deprecated))
#else
# define DEPRECATED__prototype_interfaces__msg__Prototype __declspec(deprecated)
#endif

namespace prototype_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Prototype_
{
  using Type = Prototype_<ContainerAllocator>;

  explicit Prototype_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : content(_init),
    image(_init)
  {
    (void)_init;
  }

  explicit Prototype_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : content(_alloc, _init),
    image(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _content_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _content_type content;
  using _image_type =
    sensor_msgs::msg::Image_<ContainerAllocator>;
  _image_type image;

  // setters for named parameter idiom
  Type & set__content(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->content = _arg;
    return *this;
  }
  Type & set__image(
    const sensor_msgs::msg::Image_<ContainerAllocator> & _arg)
  {
    this->image = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    prototype_interfaces::msg::Prototype_<ContainerAllocator> *;
  using ConstRawPtr =
    const prototype_interfaces::msg::Prototype_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<prototype_interfaces::msg::Prototype_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<prototype_interfaces::msg::Prototype_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      prototype_interfaces::msg::Prototype_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<prototype_interfaces::msg::Prototype_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      prototype_interfaces::msg::Prototype_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<prototype_interfaces::msg::Prototype_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<prototype_interfaces::msg::Prototype_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<prototype_interfaces::msg::Prototype_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__prototype_interfaces__msg__Prototype
    std::shared_ptr<prototype_interfaces::msg::Prototype_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__prototype_interfaces__msg__Prototype
    std::shared_ptr<prototype_interfaces::msg::Prototype_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Prototype_ & other) const
  {
    if (this->content != other.content) {
      return false;
    }
    if (this->image != other.image) {
      return false;
    }
    return true;
  }
  bool operator!=(const Prototype_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Prototype_

// alias to use template instance with default allocator
using Prototype =
  prototype_interfaces::msg::Prototype_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace prototype_interfaces

#endif  // PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__STRUCT_HPP_
