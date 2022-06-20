import 'package:dio/dio.dart';
import 'package:flutter_toman/common/http_response_validator.dart';
import 'package:flutter_toman/data/product.dart';

abstract class IProductDataSource {
  Future<SubmitProductResponse> submit(SubmitProductParams params);
}

class ProductRemoteDataSource
    with HttpResponseValidation
    implements IProductDataSource {
  final Dio httpClient;

  ProductRemoteDataSource(this.httpClient);

  @override
  Future<SubmitProductResponse> submit(SubmitProductParams params) async {
    final response =
        await httpClient.post('d1055cef-c469-49ed-835f-3a55d06f86f1', data: {
      'title': params.title,
      'price_tomans': params.price,
      'description': params.description,
    });

    validateResposnse(response);
    return SubmitProductResponse(message: 'محصول با موفقیت ثبت شد');
  }
}
