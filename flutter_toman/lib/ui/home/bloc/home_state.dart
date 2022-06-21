part of 'home_bloc.dart';

abstract class HomeState extends Equatable {
  final bool isChecked;
  const HomeState(this.isChecked);

  @override
  List<Object> get props => [isChecked];
}

class HomeInitial extends HomeState {
  const HomeInitial(bool isChecked) : super(isChecked);
}

class HomeSubmitLoading extends HomeState {
  const HomeSubmitLoading(bool isChecked) : super(isChecked);
}

class HomeSubmitSuccess extends HomeState {
  final SubmitProductResponse response;

  const HomeSubmitSuccess(this.response, bool isChecked) : super(isChecked);

  @override
  List<Object> get props => [response];
}

class HomeSubmitError extends HomeState {
  final AppException appException;

  const HomeSubmitError(this.appException, bool isChecked) : super(isChecked);

  @override
  List<Object> get props => [appException];
}

class HomeChangeCheckedRules extends HomeState {
  const HomeChangeCheckedRules(bool isChecked) : super(isChecked);
}
