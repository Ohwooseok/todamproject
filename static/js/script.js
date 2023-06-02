function showPopup(message) {
    var popup = document.createElement("div");
    popup.classList.add("popup");
    popup.innerText = message;
    document.body.appendChild(popup);

    setTimeout(function () {
      document.body.removeChild(popup);
    }, 2000);
  }

  // JavaScript function to handle the login button click

  document.addEventListener("DOMContentLoaded", function () {
    const Log_in_Button = document.querySelector(".Log_in_Button");
    const popupContainer = document.querySelector(".Log_in_PopupContainer");
    const popupContent = document.querySelector(".Log_in_PopupContent");
    const idBoxContents = document.querySelector(".Log_in_IDBOX_Contents");
    const pwBoxContents = document.querySelector(".Log_in_PWBOX_Contents");

    Log_in_Button.addEventListener("click", function () {
      popupContainer.style.display = "flex";
      popupContent.style.display = "block";
    });

    const loginForm = document.querySelector(".login-form");
    console.log(loginForm)

    const jsonLogin = async (requestBody) => {
      const response = await fetch("http://localhost:8080/auth/login", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(requestBody),
      });
      return response;
    };

    const formLogin = async (formData) => {
      const response = await fetch("http://localhost:8080/auth/login", {
        method: "post",
        headers: {
          "Content-type": "applicaiton/x-www-from-urlencoded;charset=UTF-8",
        },
        body: formData,
      });
      return response;
    };

    loginForm.addEventListener("submit", (event) => {
      event.preventDefault();

      const id_in = idBoxContents.value;
      const pw_in = pwBoxContents.value;

      if (
        id_in.length < 4 ||
        id_in.length > 30 ||
        pw_in.length < 4 ||
        pw_in.length > 30
      ) {
        const notification = document.querySelector(".Log_in_Notification");
        notification.textContent =
          "Enter proper ID and PW, which should be within 4~30 characters.";
        notification.style.color = "red";
        return;
      } else {
        // Perform login or further processing
        <!-- -[주석!!!!!!!!!! id_in이랑 pw_in이 저장됬는지 notification으로 출력되는 부분이예요.]- -->

        // json
        const loginData = {
          id: id_in,
          password: pw_in,
        };
        const response = jsonLogin(loginData);

        // //form
        // const formData = `id=${encodeURIComponent(
        //   id_in
        // )}&pw=${encodeURIComponent(pw_in)}`;
        // const response = formLogin(formData);
        alert("아이디 또는 비밀번호가 맞지 않습니다.");
      }
    });

    // const loginButton = document.querySelector(".Log_in_Login_Button");

    // loginButton.addEventListener("click", function () {
    //   const id_in = idBoxContents.value;
    //   const pw_in = pwBoxContents.value;

    //   if (
    //     id_in.length < 4 ||
    //     id_in.length > 30 ||
    //     pw_in.length < 4 ||
    //     pw_in.length > 30
    //   ) {
    //     const notification = document.querySelector(".Log_in_Notification");
    //     notification.textContent =
    //       "Enter proper ID and PW, which should be within 4~30 characters.";
    //     notification.style.color = "red";
    //   } else {
    //     // Perform login or further processing
    //     <!-- -[주석!!!!!!!!!! id_in이랑 pw_in이 저장됬는지 notification으로 출력되는 부분이예요.]- -->
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

  // JavaScript function to close the popup
  function closePopup() {
    var popup = document.querySelector(".popup");
    if (popup) {
      document.body.removeChild(popup);
    }
  }

  //  url로 회원가입을 팝업으로 띄우는 코드
  function popupOpen() {
    var popUrl = "signup";
    var popOption =
      "width=500px, height=685.576171875, resizable=no, scrollbars=no, status=no;";
    window.open(popUrl, "", popOption);
  }