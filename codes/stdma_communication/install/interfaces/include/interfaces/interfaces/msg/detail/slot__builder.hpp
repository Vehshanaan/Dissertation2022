// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Slot.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__SLOT__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__SLOT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/slot__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Slot_occupied
{
public:
  explicit Init_Slot_occupied(::interfaces::msg::Slot & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::Slot occupied(::interfaces::msg::Slot::_occupied_type arg)
  {
    msg_.occupied = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Slot msg_;
};

class Init_Slot_sender_no
{
public:
  explicit Init_Slot_sender_no(::interfaces::msg::Slot & msg)
  : msg_(msg)
  {}
  Init_Slot_occupied sender_no(::interfaces::msg::Slot::_sender_no_type arg)
  {
    msg_.sender_no = std::move(arg);
    return Init_Slot_occupied(msg_);
  }

private:
  ::interfaces::msg::Slot msg_;
};

class Init_Slot_slot_total
{
public:
  explicit Init_Slot_slot_total(::interfaces::msg::Slot & msg)
  : msg_(msg)
  {}
  Init_Slot_sender_no slot_total(::interfaces::msg::Slot::_slot_total_type arg)
  {
    msg_.slot_total = std::move(arg);
    return Init_Slot_sender_no(msg_);
  }

private:
  ::interfaces::msg::Slot msg_;
};

class Init_Slot_slot_no
{
public:
  Init_Slot_slot_no()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Slot_slot_total slot_no(::interfaces::msg::Slot::_slot_no_type arg)
  {
    msg_.slot_no = std::move(arg);
    return Init_Slot_slot_total(msg_);
  }

private:
  ::interfaces::msg::Slot msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Slot>()
{
  return interfaces::msg::builder::Init_Slot_slot_no();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__SLOT__BUILDER_HPP_
