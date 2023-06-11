// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/MapLocationUpdate.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/map_location_update__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_MapLocationUpdate_Request_y
{
public:
  explicit Init_MapLocationUpdate_Request_y(::interfaces::srv::MapLocationUpdate_Request & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::MapLocationUpdate_Request y(::interfaces::srv::MapLocationUpdate_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::MapLocationUpdate_Request msg_;
};

class Init_MapLocationUpdate_Request_x
{
public:
  explicit Init_MapLocationUpdate_Request_x(::interfaces::srv::MapLocationUpdate_Request & msg)
  : msg_(msg)
  {}
  Init_MapLocationUpdate_Request_y x(::interfaces::srv::MapLocationUpdate_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_MapLocationUpdate_Request_y(msg_);
  }

private:
  ::interfaces::srv::MapLocationUpdate_Request msg_;
};

class Init_MapLocationUpdate_Request_applicant
{
public:
  Init_MapLocationUpdate_Request_applicant()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MapLocationUpdate_Request_x applicant(::interfaces::srv::MapLocationUpdate_Request::_applicant_type arg)
  {
    msg_.applicant = std::move(arg);
    return Init_MapLocationUpdate_Request_x(msg_);
  }

private:
  ::interfaces::srv::MapLocationUpdate_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::MapLocationUpdate_Request>()
{
  return interfaces::srv::builder::Init_MapLocationUpdate_Request_applicant();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_MapLocationUpdate_Response_success
{
public:
  Init_MapLocationUpdate_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::MapLocationUpdate_Response success(::interfaces::srv::MapLocationUpdate_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::MapLocationUpdate_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::MapLocationUpdate_Response>()
{
  return interfaces::srv::builder::Init_MapLocationUpdate_Response_success();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__BUILDER_HPP_
