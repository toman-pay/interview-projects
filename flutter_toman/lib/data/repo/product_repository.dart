import 'package:flutter_toman/common/http_client.dart';
import 'package:flutter_toman/data/product.dart';
import 'package:flutter_toman/data/source/product_data_source.dart';

final productRepository = ProductRepository(ProductRemoteDataSource(httpClient));

abstract class IProductRepository extends IProductDataSource {}

class ProductRepository implements IProductRepository {
  final IProductDataSource dataSource;

  ProductRepository(this.dataSource);

  @override
  Future<SubmitProductResponse> submit(SubmitProductParams params) => dataSource.submit(params);
}

  