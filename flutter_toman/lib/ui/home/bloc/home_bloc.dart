import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter_toman/common/exception.dart';
import 'package:flutter_toman/data/product.dart';
import 'package:flutter_toman/data/repo/product_repository.dart';

part 'home_event.dart';
part 'home_state.dart';

class HomeBloc extends Bloc<HomeEvent, HomeState> {
  bool isChecked;
  final IProductRepository repository;

  HomeBloc(this.repository, {this.isChecked = false}) : super(HomeInitial(isChecked)) {
    on<HomeEvent>((event, emit) async {
      try {
        if (event is HomeSubmitProduct) {
          emit(HomeSubmitLoading(isChecked));
          final response = await repository.submit(event.params);
          emit(HomeSubmitSuccess(response, isChecked));
        }else if (event is HomeRulesClicked) {
          isChecked = !isChecked;
          emit(HomeChangeCheckedRules(isChecked));
        }
      } catch (e) {
        emit(HomeSubmitError(AppException(), isChecked));
      }
    });
  }
}
