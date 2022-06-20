part of 'home_bloc.dart';

abstract class HomeEvent extends Equatable {
  const HomeEvent();

  @override
  List<Object> get props => [];
}

class HomeSubmitProduct extends HomeEvent {
  final SubmitProductParams params;

  const HomeSubmitProduct(this.params);

  @override
  List<Object> get props => [params];
}
