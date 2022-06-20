import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter_toman/common/exception.dart';
import 'package:flutter_toman/data/product.dart';
import 'package:flutter_toman/data/repo/product_repository.dart';

part 'home_event.dart';
part 'home_state.dart';

class HomeBloc extends Bloc<HomeEvent, HomeState> {
  final IProductRepository repository;

  HomeBloc(this.repository) : super(HomeInitial()) {
    on<HomeEvent>((event, emit) async {
      if (event is HomeSubmitProduct) {
        try {
          emit(HomeSubmitLoading());
          final response = await repository.submit(event.params);
          emit(HomeSubmitSuccess(response));
        } catch (e) {
          emit(HomeSubmitError(AppException()));
        }
      }
    });
  }
}
