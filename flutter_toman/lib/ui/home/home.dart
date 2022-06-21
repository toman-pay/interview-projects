import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:flutter_toman/common/utils.dart';
import 'package:flutter_toman/data/product.dart';
import 'package:flutter_toman/data/repo/product_repository.dart';
import 'package:flutter_toman/theme.dart';
import 'package:flutter_toman/ui/home/bloc/home_bloc.dart';
import 'package:flutter_toman/ui/rules/rules.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  HomeBloc? bloc;
  StreamSubscription? subscription;
  final ScrollController _scrollController = ScrollController();
  final TextEditingController priceController = TextEditingController(text: '');
  final TextEditingController titleController = TextEditingController(text: '');
  final TextEditingController descriptionCntroller =
      TextEditingController(text: '');
  final formKey = GlobalKey<FormState>();

  @override
  void dispose() {
    bloc?.close();
    subscription?.cancel();
    priceController.dispose();
    titleController.dispose();
    descriptionCntroller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);
    return BlocProvider<HomeBloc>(
      create: (context) {
        bloc = HomeBloc(productRepository);
        subscription = bloc?.stream.listen((state) {
          if (state is HomeSubmitError) {
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                duration: const Duration(seconds: 1),
                content: Text(
                  state.appException.message,
                )));
          } else if (state is HomeSubmitSuccess) {
            priceController.clear();
            titleController.clear();
            descriptionCntroller.clear();
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                duration: const Duration(seconds: 2),
                content: Text(
                  state.response.message,
                )));
          }
        });
        return bloc!;
      },
      child: Scaffold(
        backgroundColor: themeData.colorScheme.surfaceVariant,
        appBar: AppBar(
            centerTitle: true,
            title: Text(
              'ساخت تراکنش',
              style: themeData.textTheme.subtitle2!
                  .copyWith(fontWeight: FontWeight.w500),
            )),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
        floatingActionButton: SizedBox(
            width: MediaQuery.of(context).size.width - 48,
            child: BlocBuilder<HomeBloc, HomeState>(
              builder: (context, state) {
                return FloatingActionButton.extended(
                    backgroundColor: state.isChecked
                        ? LightThemeColors.primaryColor
                        : LightThemeColors.secondryColor,
                    onPressed: state.isChecked
                        ? () {
                            if (formKey.currentState?.validate() ?? false) {
                              bloc?.add(HomeSubmitProduct(
                                SubmitProductParams(
                                    title: titleController.text.trim(),
                                    price: priceController.text.isNotEmpty
                                        ? int.parse(priceController.text
                                            .replaceAll(',', ''))
                                        : 0,
                                    description:
                                        descriptionCntroller.text.trim()),
                              ));
                            }
                          }
                        : null,
                    label: state is HomeSubmitLoading
                        ? Center(
                            child: CupertinoActivityIndicator(
                              color: themeData.colorScheme.onSecondary,
                            ),
                          )
                        : const Text(
                            'تایید',
                          ));
              },
            )),
        body: SingleChildScrollView(
            physics: defaultScrollPhsics,
            child: Form(
              key: formKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Divider(
                    height: 1,
                  ),
                  Padding(
                    padding: const EdgeInsets.only(top: 32, right: 24),
                    child: Row(
                      children: [
                        Stack(
                          alignment: Alignment.bottomCenter,
                          children: [
                            SvgPicture.asset(
                              'assets/img/icon2.svg',
                              width: 24,
                            ),
                            Positioned(
                                bottom: 5,
                                child: SvgPicture.asset(
                                  'assets/img/icon1.svg',
                                  width: 7,
                                )),
                          ],
                        ),
                        const SizedBox(
                          width: 12,
                        ),
                        Text(
                          'اطلاعات محصول',
                          style: themeData.textTheme.subtitle2!
                              .copyWith(fontWeight: FontWeight.bold),
                        )
                      ],
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(right: 24, top: 40),
                    child: Text('عنوان محصول',
                        style: themeData.textTheme.subtitle2!
                            .copyWith(fontWeight: FontWeight.w500)),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(left: 24, right: 24, top: 8),
                    child: TextFormField(
                      inputFormatters: [LengthLimitingTextInputFormatter(30)],
                      validator: (value) {
                        if (value!.isEmpty) {
                          return 'عنوان محصول را وارد کنید';
                        }
                        return null;
                      },
                      controller: titleController,
                      decoration: const InputDecoration(
                          contentPadding:
                              EdgeInsets.only(bottom: 5, right: 10)),
                      textAlignVertical: TextAlignVertical.center,
                      style: themeData.textTheme.bodyText2!
                          .copyWith(fontWeight: FontWeight.w400),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(right: 24, top: 12),
                    child: Text('قیمت',
                        style: themeData.textTheme.subtitle2!
                            .copyWith(fontWeight: FontWeight.w500)),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(left: 24, right: 24, top: 8),
                    child: TextFormField(
                        validator: (value) {
                          if (value!.isEmpty) {
                            return 'قیمت محصول را وارد کنید';
                          }
                          return null;
                        },
                        controller: priceController,
                        inputFormatters: [
                          FilteringTextInputFormatter.digitsOnly,
                          LengthLimitingTextInputFormatter(15)
                        ],
                        onChanged: (value) {
                          if (value.isNotEmpty) {
                            value = value.replaceAll(',', '').numberFormat;
                          }
                          priceController.value = TextEditingValue(
                            text: value,
                            selection:
                                TextSelection.collapsed(offset: value.length),
                          );
                        },
                        style: themeData.textTheme.bodyText2!
                            .copyWith(fontWeight: FontWeight.w400),
                        decoration: InputDecoration(
                          contentPadding: const EdgeInsets.only(
                              bottom: 5, right: 10, left: 10),
                          suffixText: 'تومان',
                          suffixStyle: themeData.textTheme.subtitle2!
                              .apply(color: LightThemeColors.secondryTextColor),
                        )),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(right: 24, top: 12),
                    child: Text('توضیحات',
                        style: themeData.textTheme.subtitle2!
                            .copyWith(fontWeight: FontWeight.w500)),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(left: 24, right: 24, top: 8),
                    child: Scrollbar(
                      controller: _scrollController,
                      child: TextField(
                        controller: descriptionCntroller,
                        scrollPadding: const EdgeInsets.only(bottom: 80),
                        decoration: const InputDecoration(
                            contentPadding: EdgeInsets.all(10)),
                        style: themeData.textTheme.bodyText2!
                            .copyWith(fontWeight: FontWeight.w400, height: 1.5),
                        scrollController: _scrollController,
                        maxLines: 3,
                      ),
                    ),
                  ),
                  const SizedBox(
                    height: 16,
                  ),
                  BlocBuilder<HomeBloc, HomeState>(
                    buildWhen: (previous, current) =>
                        current is HomeChangeCheckedRules,
                    builder: (context, state) {
                      return CheckboxListTile(
                          activeColor: LightThemeColors.primaryColor,
                          title: RichText(
                            text: TextSpan(
                                recognizer: TapGestureRecognizer()
                                  ..onTap = () {
                                    showModalBottomSheet(
                                        shape: const RoundedRectangleBorder(
                                            borderRadius: BorderRadius.vertical(
                                                top: Radius.circular(24))),
                                        context: context,
                                        builder: (context) {
                                          return const RulesScreen();
                                        });
                                  },
                                text: 'شرایط و قوانین ',
                                style: themeData.textTheme.subtitle2!.copyWith(
                                    color: LightThemeColors.primaryColor,
                                    fontWeight: FontWeight.w700),
                                children: [
                                  TextSpan(
                                    text: 'را می پذیرم.',
                                    style: themeData.textTheme.subtitle2!
                                        .copyWith(fontWeight: FontWeight.w500),
                                  )
                                ]),
                          ),
                          controlAffinity: ListTileControlAffinity.leading,
                          value: state.isChecked ? true : false,
                          onChanged: (value) {
                            bloc?.add(const HomeRulesClicked());
                          });
                    },
                  ),
                ],
              ),
            )),
      ),
    );
  }
}
