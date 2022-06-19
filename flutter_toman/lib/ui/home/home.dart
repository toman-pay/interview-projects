import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:flutter_toman/common/utils.dart';
import 'package:flutter_toman/theme.dart';
import 'package:flutter_toman/ui/rules/rules.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);
    final ScrollController _scrollController = ScrollController();
    final TextEditingController priceController = TextEditingController();

    return Scaffold(
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
          child: FloatingActionButton.extended(
              onPressed: () {},
              label: const Text(
                'تایید',
              ))),
      body: SingleChildScrollView(
          physics: defaultScrollPhsics,
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
              SizedBox(
                height: 56,
                child: Padding(
                  padding: const EdgeInsets.only(left: 24, right: 24, top: 8),
                  child: TextField(
                    decoration: const InputDecoration(
                        contentPadding: EdgeInsets.only(bottom: 5, right: 10)),
                    textAlignVertical: TextAlignVertical.center,
                    style: themeData.textTheme.bodyText2!
                        .copyWith(fontWeight: FontWeight.w400),
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(right: 24, top: 12),
                child: Text('قیمت',
                    style: themeData.textTheme.subtitle2!
                        .copyWith(fontWeight: FontWeight.w500)),
              ),
              SizedBox(
                height: 56,
                child: Padding(
                  padding: const EdgeInsets.only(left: 24, right: 24, top: 8),
                  child: TextField(
                      keyboardType: TextInputType.number,
                      inputFormatters: [FilteringTextInputFormatter.digitsOnly],
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
                      controller: priceController,
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
              CheckboxListTile(
                  activeColor: LightThemeColors.primaryColor,
                  title: InkWell(
                    onTap: () {
                      showModalBottomSheet(
                          shape: const RoundedRectangleBorder(
                              borderRadius: BorderRadius.vertical(
                                  top: Radius.circular(24))),
                          context: context,
                          builder: (context) {
                            return const RulesScreen();
                          });
                    },
                    child: RichText(
                      text: TextSpan(
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
                  ),
                  controlAffinity: ListTileControlAffinity.leading,
                  value: true,
                  onChanged: (value) {}),
            ],
          )),
    );
  }
}
