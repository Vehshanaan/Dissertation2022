// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from prototype_interfaces:action/PrototypeAction.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__ACTION__DETAIL__PROTOTYPE_ACTION__BUILDER_HPP_
#define PROTOTYPE_INTERFACES__ACTION__DETAIL__PROTOTYPE_ACTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "prototype_interfaces/action/detail/prototype_action__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace prototype_interfaces
{

namespace action
{

namespace builder
{

class Init_PrototypeAction_Goal_order
{
public:
  Init_PrototypeAction_Goal_order()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::prototype_interfaces::action::PrototypeAction_Goal order(::prototype_interfaces::action::PrototypeAction_Goal::_order_type arg)
  {
    msg_.order = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::action::PrototypeAction_Goal>()
{
  return prototype_interfaces::action::builder::Init_PrototypeAction_Goal_order();
}

}  // namespace prototype_interfaces


namespace prototype_interfaces
{

namespace action
{

namespace builder
{

class Init_PrototypeAction_Result_sequence
{
public:
  Init_PrototypeAction_Result_sequence()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::prototype_interfaces::action::PrototypeAction_Result sequence(::prototype_interfaces::action::PrototypeAction_Result::_sequence_type arg)
  {
    msg_.sequence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::action::PrototypeAction_Result>()
{
  return prototype_interfaces::action::builder::Init_PrototypeAction_Result_sequence();
}

}  // namespace prototype_interfaces


namespace prototype_interfaces
{

namespace action
{

namespace builder
{

class Init_PrototypeAction_Feedback_partial_sequence
{
public:
  Init_PrototypeAction_Feedback_partial_sequence()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::prototype_interfaces::action::PrototypeAction_Feedback partial_sequence(::prototype_interfaces::action::PrototypeAction_Feedback::_partial_sequence_type arg)
  {
    msg_.partial_sequence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::action::PrototypeAction_Feedback>()
{
  return prototype_interfaces::action::builder::Init_PrototypeAction_Feedback_partial_sequence();
}

}  // namespace prototype_interfaces


namespace prototype_interfaces
{

namespace action
{

namespace builder
{

class Init_PrototypeAction_SendGoal_Request_goal
{
public:
  explicit Init_PrototypeAction_SendGoal_Request_goal(::prototype_interfaces::action::PrototypeAction_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::prototype_interfaces::action::PrototypeAction_SendGoal_Request goal(::prototype_interfaces::action::PrototypeAction_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_SendGoal_Request msg_;
};

class Init_PrototypeAction_SendGoal_Request_goal_id
{
public:
  Init_PrototypeAction_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PrototypeAction_SendGoal_Request_goal goal_id(::prototype_interfaces::action::PrototypeAction_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_PrototypeAction_SendGoal_Request_goal(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::action::PrototypeAction_SendGoal_Request>()
{
  return prototype_interfaces::action::builder::Init_PrototypeAction_SendGoal_Request_goal_id();
}

}  // namespace prototype_interfaces


namespace prototype_interfaces
{

namespace action
{

namespace builder
{

class Init_PrototypeAction_SendGoal_Response_stamp
{
public:
  explicit Init_PrototypeAction_SendGoal_Response_stamp(::prototype_interfaces::action::PrototypeAction_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::prototype_interfaces::action::PrototypeAction_SendGoal_Response stamp(::prototype_interfaces::action::PrototypeAction_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_SendGoal_Response msg_;
};

class Init_PrototypeAction_SendGoal_Response_accepted
{
public:
  Init_PrototypeAction_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PrototypeAction_SendGoal_Response_stamp accepted(::prototype_interfaces::action::PrototypeAction_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_PrototypeAction_SendGoal_Response_stamp(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::action::PrototypeAction_SendGoal_Response>()
{
  return prototype_interfaces::action::builder::Init_PrototypeAction_SendGoal_Response_accepted();
}

}  // namespace prototype_interfaces


namespace prototype_interfaces
{

namespace action
{

namespace builder
{

class Init_PrototypeAction_GetResult_Request_goal_id
{
public:
  Init_PrototypeAction_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::prototype_interfaces::action::PrototypeAction_GetResult_Request goal_id(::prototype_interfaces::action::PrototypeAction_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::action::PrototypeAction_GetResult_Request>()
{
  return prototype_interfaces::action::builder::Init_PrototypeAction_GetResult_Request_goal_id();
}

}  // namespace prototype_interfaces


namespace prototype_interfaces
{

namespace action
{

namespace builder
{

class Init_PrototypeAction_GetResult_Response_result
{
public:
  explicit Init_PrototypeAction_GetResult_Response_result(::prototype_interfaces::action::PrototypeAction_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::prototype_interfaces::action::PrototypeAction_GetResult_Response result(::prototype_interfaces::action::PrototypeAction_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_GetResult_Response msg_;
};

class Init_PrototypeAction_GetResult_Response_status
{
public:
  Init_PrototypeAction_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PrototypeAction_GetResult_Response_result status(::prototype_interfaces::action::PrototypeAction_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_PrototypeAction_GetResult_Response_result(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::action::PrototypeAction_GetResult_Response>()
{
  return prototype_interfaces::action::builder::Init_PrototypeAction_GetResult_Response_status();
}

}  // namespace prototype_interfaces


namespace prototype_interfaces
{

namespace action
{

namespace builder
{

class Init_PrototypeAction_FeedbackMessage_feedback
{
public:
  explicit Init_PrototypeAction_FeedbackMessage_feedback(::prototype_interfaces::action::PrototypeAction_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::prototype_interfaces::action::PrototypeAction_FeedbackMessage feedback(::prototype_interfaces::action::PrototypeAction_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_FeedbackMessage msg_;
};

class Init_PrototypeAction_FeedbackMessage_goal_id
{
public:
  Init_PrototypeAction_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PrototypeAction_FeedbackMessage_feedback goal_id(::prototype_interfaces::action::PrototypeAction_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_PrototypeAction_FeedbackMessage_feedback(msg_);
  }

private:
  ::prototype_interfaces::action::PrototypeAction_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::action::PrototypeAction_FeedbackMessage>()
{
  return prototype_interfaces::action::builder::Init_PrototypeAction_FeedbackMessage_goal_id();
}

}  // namespace prototype_interfaces

#endif  // PROTOTYPE_INTERFACES__ACTION__DETAIL__PROTOTYPE_ACTION__BUILDER_HPP_
