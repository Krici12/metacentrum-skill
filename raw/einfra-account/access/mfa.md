#

## [MFA Advantages](#mfa-advantages)

You can **enhance the security of your e-INFRA CZ Account by enabling Multi-Factor Authentication (MFA)**. MFA adds an additional verification step during login, making unauthorized access significantly harder. **Some services in the e-INFRA CZ infrastructure require MFA to be enabled.**

The e-INFRA CZ AAI (Authentication and Authorization Infrastructure) supports two MFA methods:

- **TOTP** (Time-based One-Time Password)

- **WebAuthn** (Web Authentication, button press, fingerprint, etc.)

Check our interactive guide to help you choose the right MFA method based on your device and preference.

### [TOTP (Time-based One-Time Password) Setting](#totp-time-based-one-time-password-setting)

TOTP is a widely used standard where a mobile or desktop app generates 6-digit codes that change every 30 seconds. These codes are generated based on a shared secret between your device and our servers.

Also Known As

You might recognize TOTP under other names such as:

- Verification code

- Authenticator code

- 6-digit code from code generator or Google Authenticator

- Code from authentication/verification app

- Works across multiple platforms (PC, mobile, tablet)

- Compatible with many authenticator apps

- Offline capable (no need for an internet connection)

#### [Supported Apps](#supported-apps)

Choose any of the following TOTP-compatible apps:

- [andOTP](https://sourceforge.net/projects/andotp.mirror/)

- [Aegis Authenticator](https://play.google.com/store/apps/details?id=com.beemdevelopment.aegis)

- [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2)

- [FreeOTP+](https://play.google.com/store/apps/details?id=org.liberty.android.freeotpplus)

Or use the TOTP functionality built into password managers:

- [BitWarden](https://bitwarden.com/help/integrated-authenticator/)

- [LastPass Authenticator](https://www.lastpass.com/solutions/authentication)

If you already use a TOTP app, simply add your e-INFRA CZ account. No need to install another.

TOTP is standardized in [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238)

### [WebAuthn (Web Authentication) Setting](#webauthn-web-authentication-setting)

WebAuthn is often integrated into modern operating systems and browsers.

In order to use WebAuthn, you need to use one of the supported web browsers together with the operating system capability, an app or a physical authenticator (e.g. a YubiKey).

- A hardware token (e.g. [YubiKey](https://www.yubico.com/authentication-standards/fido2/))

- No codes to type — just confirm with your device (button press, fingerprint, etc.)

- Built into many devices and platforms

- Extremely secure against phishing and account takeover

- Built-in platform authentication (e.g. Windows Hello, macOS Touch ID)

Also Known As

WebAuthn may also appear under other names like:

- FIDO2

- U2F (Universal 2nd Factor)

- Security key

- USB security key
Learn more at [webauthn.io](https://webauthn.io) and [webauthn.me](https://webauthn.me/).

WebAuth Support in various OS

- **Windows 10+**: Use [Windows Hello](https://support.microsoft.com/en-us/windows/configure-windows-hello-dae28983-8242-bb2a-d3d1-87c9d265a5f0) using a PIN, facial recognition, or fingerprint. Windows 10 build 1903 or later is required.

- **macOS 10.15+**: [Touch ID](https://support.apple.com/en-in/guide/mac-help/mchl16fbf90a/mac) feature can be used (Chrome, Safari).

- **Android 7+**: Requires [screen lock](https://support.google.com/android/answer/9079129?hl=en) (PIN, pattern, fingerprint, face)

- **iOS 14.5+**: Touch ID / Face ID

- **Linux**: Use USB-based FIDO2 tokens (e.g., Yubikey]([https://www.yubico.com/authentication-standards/fido2/](https://www.yubico.com/authentication-standards/fido2/))) Bluetooth enabled on both devices, Google Chrome browser on both, and the phone to be in close proximity to the PC. If your Android Chrome browser has an authenticated Google Account, screen lock methods can be used for the second factor; otherwise, you can scan a one-time QR code from the PC screen with your phone.

- Alternatively a NFC or USB connected hardware token like [Yubikey](https://www.yubico.com/authentication-standards/fido2/) can be used.

## [How to Set MFA in Perun](#how-to-set-mfa-in-perun)

Register at least one token. Your **first token must be TOTP**.

Once you register your first token, MFA will be required whenever you log in to manage or modify your MFA settings.

### [Register Your First Token](#register-your-first-token)

-

Visit the [MFA Management Page](https://mfa.login.e-infra.cz), *or* go to your [e-INFRA CZ User Profile](https://profile.e-infra.cz/profile) and navigate to `Authentication` -> `Multi-Factor Autentication (MFA)`

-

Click on `Manage my MFA tokens` and sign in with your identity from your home institution.

-

Click **Log In** to enter the MFA management application (privacyIDEA).
![Login as](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadd01.2s6090p5fozvk.jpeg&w=3840&q=75)

-

Choose **Enroll Token** in the left menu
![List token](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadd02.0tpxs5pvikgfh.jpeg&w=3840&q=75)

-

Select **TOTP**, enter a description, and click **Enroll Token**.
![List token2](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadd03.1t-nla3pljefy.jpeg&w=3840&q=75)

-

Scan the displayed QR code with your TOTP app.

- If using a mobile device, you can tap the link to open the TOTP app directly.

You can add more TOTP apps later — a new QR code will be generated.

![QR code](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadd04.2786iq47zb-05.jpeg&w=3840&q=75)

Next time you log in, MFA will be required using this token.

### [Add More Tokens](#add-more-tokens)

-

Click **Enroll Token** again.

-

Choose **WebAuthn** (if supported), enter a description, and click **Enroll Token**.
![Add token](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadd05.0b8xgjse1kqrx.jpeg&w=3840&q=75)

-

Confirm registration using your device (e.g., fingerprint, hardware token).
![Add token2](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadd06.309siicup_xe1.jpeg&w=3840&q=75)

-

After successful registration a confirmation appears.
![Add token3](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadd07.43jo1v5awtp84.jpeg&w=3840&q=75)

We **strongly recommend** registering at least two tokens, including one TOTP app, to prevent lockout.

### [Prepare Recovery Codes](#prepare-recovery-codes)

To regain access if you lose all tokens, generate and securely store **one-time recovery codes**.

-

Click **Enroll Token**
![Recovery](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frecovery01.0tpxs5pvikgfh.jpeg&w=3840&q=75)

-

Select `PPR: One Time Passwords printed on sheet of paper`, provide a description, and click **Enroll Token**.
![Recovery2](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frecovery02.1rc0pjz29sc1r.jpeg&w=3840&q=75)

-

View or print the codes by clicking `The OTP Values` or `Print the OTP list`.
![Recovery3](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frecovery03.2zeaf4r5fw5bk.jpeg&w=3840&q=75)

Recovery codes.

To prevent being locked out of your account, we strongly recommend generating one-time **recovery codes** in case you lose access to your MFA tokens. See the [Recovery Codes section](#recovery-codes) for more information.

### [Enable or Disable MFA for (All) Services](#enable-or-disable-mfa-for-all-services)

MFA is required:

- If a **service mandates it**, or

- If **you explicitly enable it** in your account settings

To enable MFA globally:

- Go to your [e-INFRA CZ User Profile](https://profile.e-infra.cz/)

- Navigate to `Authentication` -> `Multi-Factor Autentication (MFA)`

- Toggle `Turn on multi-factor authentication for all services`
![Toggle](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftoggle.14nqg7_zojnr4.png&w=3840&q=75)

## [Perform MFA](#perform-mfa)

### [When Is MFA Required?](#when-is-mfa-required)

- When accessing services that require MFA

- When you enable MFA for all services

- When managing MFA settings or tokens

### [How to Log in Using MFA](#how-to-log-in-using-mfa)

- Log in using your home organization or e-INFRA CZ credentials.

- If MFA is required, you’ll be prompted to verify using TOTP or WebAuthn.

![MFA](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmfa.19-ibk_1xkc9k.png&w=3840&q=75)

Both options `TOTP` and `WebAuthn` are displayed, and you must pick the one based on the type of MFA token you registered and have available at the moment. You can have both types of tokens registered; in such a case, you can choose any of the options.

If you have no valid tokens or authentication fails, you will receive an error message.

### [MFA with Home Organization Login](#mfa-with-home-organization-login)

If your **home institution** supports MFA and releases that information during login, you **don’t need to repeat MFA** within e-INFRA CZ.

Currently, this is supported only by **Masaryk University**.

Important

You must still register at least one MFA token with your e-INFRA CZ Account to retain access if your affiliation changes.

MFA tokens managed by your home organization are **not supported by us**, and we **cannot assist** if you lose access to them.

Do **not** register shared or employer-owned MFA tokens (e.g., company-issued YubiKeys) unless you are sure they are your personal devices.

![publicity banner](/_next/static/media/einfra_4loga-zapati.2rmjkbgplixgm.svg)

### On this page
[MFA Advantages](#mfa-advantages)[TOTP (Time-based One-Time Password) Setting](#totp-time-based-one-time-password-setting)[Supported Apps](#supported-apps)[WebAuthn (Web Authentication) Setting](#webauthn-web-authentication-setting)[How to Set MFA in Perun](#how-to-set-mfa-in-perun)[Register Your First Token](#register-your-first-token)[Add More Tokens](#add-more-tokens)[Prepare Recovery Codes](#prepare-recovery-codes)[Enable or Disable MFA for (All) Services](#enable-or-disable-mfa-for-all-services)[Perform MFA](#perform-mfa)[When Is MFA Required?](#when-is-mfa-required)[How to Log in Using MFA](#how-to-log-in-using-mfa)[MFA with Home Organization Login](#mfa-with-home-organization-login)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
