// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/MapSending.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MAP_SENDING__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__MAP_SENDING__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/map_sending__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_MapSending_Request_applicant
{
public:
  Init_MapSending_Request_applicant()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::MapSending_Request applicant(::interfaces::srv::MapSending_Request::_applicant_type arg)
  {
    msg_.applicant = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::MapSending_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::MapSending_Request>()
{
  return interfaces::srv::builder::Init_MapSending_Request_applicant();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_MapSending_Response_map_data
{
public:
  Init_MapSending_Response_map_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::MapSending_Response map_data(::interfaces::srv::MapSending_Response::_map_data_type arg)
  {
    msg_.map_data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::MapSending_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::MapSending_Response>()
{
  return interfaces::srv::builder::Init_MapSending_Response_map_data();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__MAP_SENDING__BUILDER_HPP_
