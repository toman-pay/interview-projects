part of 'home_bloc.dart';

abstract class HomeState extends Equatable {
  const HomeState();

  @override
  List<Object> get props => [];
}

class HomeInitial extends HomeState {}

class HomeSubmitLoading extends HomeState {}

class HomeSubmitSuccess extends HomeState {
  final SubmitProductResponse response;

  const HomeSubmitSuccess(this.response);

  @override
  List<Object> get props => [response];
}

class HomeSubmitError extends HomeState {
  final AppException appException;

  const HomeSubmitError(this.appException);

  @override
  List<Object> get props => [appException];
}
