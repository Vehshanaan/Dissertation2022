// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/MapVisualiserSiteMoves.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__MAP_VISUALISER_SITE_MOVES__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__MAP_VISUALISER_SITE_MOVES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/map_visualiser_site_moves__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_MapVisualiserSiteMoves_y
{
public:
  explicit Init_MapVisualiserSiteMoves_y(::interfaces::msg::MapVisualiserSiteMoves & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::MapVisualiserSiteMoves y(::interfaces::msg::MapVisualiserSiteMoves::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::MapVisualiserSiteMoves msg_;
};

class Init_MapVisualiserSiteMoves_x
{
public:
  explicit Init_MapVisualiserSiteMoves_x(::interfaces::msg::MapVisualiserSiteMoves & msg)
  : msg_(msg)
  {}
  Init_MapVisualiserSiteMoves_y x(::interfaces::msg::MapVisualiserSiteMoves::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_MapVisualiserSiteMoves_y(msg_);
  }

private:
  ::interfaces::msg::MapVisualiserSiteMoves msg_;
};

class Init_MapVisualiserSiteMoves_site_no
{
public:
  Init_MapVisualiserSiteMoves_site_no()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MapVisualiserSiteMoves_x site_no(::interfaces::msg::MapVisualiserSiteMoves::_site_no_type arg)
  {
    msg_.site_no = std::move(arg);
    return Init_MapVisualiserSiteMoves_x(msg_);
  }

private:
  ::interfaces::msg::MapVisualiserSiteMoves msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::MapVisualiserSiteMoves>()
{
  return interfaces::msg::builder::Init_MapVisualiserSiteMoves_site_no();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__MAP_VISUALISER_SITE_MOVES__BUILDER_HPP_
