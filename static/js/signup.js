document.addEventListener("DOMContentLoaded", function () {
    const popupContainer = document.querySelector(
      ".Sign_in_PopupContainer"
    );
    const popupContent = document.querySelector(".Sign_in_PopupContent");
    const idBoxContents = document.querySelector(".Sign_in_IDBOX_Contents");
    const pwBoxContents = document.querySelector(".Sign_in_PWBOX_Contents");
     const pwBox_check_Contents = document.querySelector(".Sign_in_PWBOX_check_Contents");
    const SigninButton = document.querySelector(".Sign_in_Sign_in_Button");

    SigninButton.addEventListener("click", function () {
      popupContainer.style.display = "none";
      popupContent.style.display = "none";
    });

    const jsonSignin = async (requestBody) => {
      const response = await fetch("http://localhost:8080/auth/signin", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(requestBody),
      });
      return response;
    };

    const formSignin = async (formString) => {
      const response = await fetch("http://localhost:8080/auth/signin", {
        method: "post",
        mode: 'cors',
        credentials: 'include',
        beforeSend: function(xhr) {
          xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken')); // CSRF 토큰을 헤더에 추가
        },
        headers: {
          "Content-type": "applicaiton/x-www-from-urlencoded;charset=UTF-8",
          'Access-Control-Allow-Origin': 'https://example.com', // 요청을 허용하는 도메인을 설정합니다.
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', // 허용되는 HTTP 메서드를 설정합니다.
          'Access-Control-Allow-Headers': 'Content-Type', // 허용되는 요청 헤더를 설정합니다.
          
        },
        body: formString,
      });
      return response;
    };

    const signinForm = document.querySelector(".sign-in-form");
    signinForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const id_in = idBoxContents.value;
      const pw_in = pwBoxContents.value;
      const pw_check_in = pwBox_check_Contents.value;

      if (pw_in !== pw_check_in) {
        const notification = document.querySelector(".Sign_in_Notification");
        notification.textContent = "비밀번호가 일치하지 않습니다";
        notification.style.color = "red";
        return;
      }

      if (
        id_in.length < 4 ||
        id_in.length > 30 ||
        pw_in.length < 4 ||
        pw_in.length > 30
      ) {
        const notification = document.querySelector(
          ".Sign_in_Notification"
        );
        notification.textContent =
          "ID와 PW는 4글자 이상 30글자 미만으로 만드세요.";
        notification.style.color = "red";
        return;
      }

      //json
      const request = {
        id: id_in,
        password: pw_in,
      };
      const response = jsonSignin(request);
      // form
      // const formString = `id=${encodeURIComponent(
      //   id_in
      // )}&password=${encodeURIComponent(pw_in)}`;
      // const response = formSignin(formString);
      // Perform login or further processing
    });

    // SigninButton.addEventListener("click", function () {
    //   const id_in = idBoxContents.value;
    //   const pw_in = pwBoxContents.value;

    //   if (
    //     id_in.length < 4 ||
    //     id_in.length > 30 ||
    //     pw_in.length < 4 ||
    //     pw_in.length > 30
    //   ) {
    //     const notification = document.querySelector(
    //       ".Sign_in_Notification"
    //     );
    //     notification.textContent =
    //       "ID와 PW는 4글자 이상 30글자 미만으로 만드세요.";
    //     notification.style.color = "red";
    //   } else {
    //     // Perform login or further processing
    //     alert("Username: " + id_in + "\nPassword: " + pw_in);
    //   }
    // });

    popupContainer.addEventListener("click", function (event) {
      if (event.target === popupContainer) {
        popupContainer.style.display = "none";
        popupContent.style.display = "none";
      }
    });
  });