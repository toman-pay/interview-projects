import React from "react"
import Drawer from "react-modern-drawer"

//import styles 👇
import "react-modern-drawer/dist/index.css"
import Button from "../button"
import "./index.scss"

const EulaDrawer = ({
  isOpen = false,
  setIsOpen = () => {},
  onAccept = () => {},
}) => {
  const closeDrawer = () => {
    setIsOpen(false)
  }

  return (
    <Drawer
      open={isOpen}
      className="eula-drawer"
      onClose={closeDrawer}
      direction="bottom"
      size={400}
    >
      <div className="indicator" />
      <div className="content">
        <div className="title">شرایط و قوانین</div>
        <div className="info">
          کاربران هر یک از سرویس های سامانه معاملات امن تومن به هر شکل و عنوان،
          مستقیم یا غیر مستقیم و جزئی یا کلی، ملزم به رعایت قوانین و مقررات حاکم
          بر کل سامانه معاملات امن تومن می باشند. در صورت تغییر این قوانین،
          جزییات این تغییرات به اطلاع کلیه کاربران خواهد رسید که از زمان ابلاغ و
          اعلام تغییرات، قوانین به روز شده در کل سامانه معاملات امن تومن، لازم
          الاجرا خواهند بود. همواره آخرین نسخه قوانین حاکم بر سامانه معاملات
          تومن، در سایت سامانه در دسترس عموم خواهد بود و قابل استناد می باشند.
        </div>
      </div>

      <Button onClick={onAccept}>شرایط و قوانین را می‌پذیرم</Button>
    </Drawer>
  )
}

export default EulaDrawer
