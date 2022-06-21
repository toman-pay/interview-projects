import 'package:flutter/material.dart';
import 'package:flutter_toman/theme.dart';

class RulesScreen extends StatelessWidget {
  const RulesScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return Directionality(
      textDirection: TextDirection.rtl,
      child: SizedBox(
        height: 470,
        child: Padding(
          padding: const EdgeInsets.fromLTRB(24, 16, 24, 16),
          child: Column(
            children: [
              Container(
                width: 24,
                height: 2,
                color: LightThemeColors.secondryTextColor,
              ),
              const SizedBox(
                height: 10,
              ),
              Text('شرایط و قوانین',
                  style: themeData.textTheme.subtitle1),
              const SizedBox(
                height: 16,
              ),
              Text(
                'کاربران هر یک از سرویس های سامانه معاملات امن تومن به هر شکل و عنوان، مستقیم یا غیر مستقیم و جزئی یا کلی، ملزم به رعایت قوانین و مقررات حاکم بر کل سامانه معاملات امن تومن می باشند. در صورت تغییر این قوانین، جزییات این تغییرات به اطلاع کلیه کاربران خواهد رسید که از زمان ابلاغ و اعلام تغییرات، قوانین به روز شده در کل سامانه معاملات امن تومن، لازم الاجرا خواهند بود. همواره آخرین نسخه قوانین حاکم بر سامانه معاملات تومن، در سایت سامانه در دسترس عموم خواهد بود و قابل استناد می باشند',
                textAlign: TextAlign.justify,
                style: themeData.textTheme.caption!
                    .copyWith(fontSize: 14, height: 1.8),
              ),
              const SizedBox(
                height: 24,
              ),
              SizedBox(
                width: MediaQuery.of(context).size.width - 48,
                height: 48,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(24)
    
                    )
                  ),
                    onPressed: () {
                      FocusManager.instance.primaryFocus!.unfocus();
                      Navigator.pop(context);
                    },
                    child: const Text(
                      'شرایط و قوانین را می پذیرم',
                    )),
              )
            ],
          ),
        ),
      ),
    );
  }
}
