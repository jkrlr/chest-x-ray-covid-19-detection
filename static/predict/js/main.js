const input = document.getElementById("id_image");

const alertBox = document.getElementById("alert-box");
const imageBox = document.getElementById("image-box");
const progressBox = document.getElementById("progress-box");
const uploadInfo = document.getElementById("upload-info");

const uploadBtn = document.getElementById("upload-btn");
const submitBtn = document.getElementById("submit-btn");

const csrf = document.getElementsByName("csrfmiddlewaretoken");

input.addEventListener("change", () => {
  progressBox.classList.remove("not-visible");
  uploadInfo.classList.add("not-visible");

  const img_data = input.files[0];
  const url = URL.createObjectURL(img_data);

  const form_data = new FormData();
  form_data.append("csrfmiddlewaretoken", csrf[0].value);
  form_data.append("image", img_data);

  $.ajax({
    type: "POST",
    enctype: "multipart/form-data",
    data: form_data,
    beforeSend: function () {
      alertBox.innerHTML = "";
      imageBox.innerHTML = "";
    },
    xhr: function () {
      const xhr = new window.XMLHttpRequest();
      xhr.upload.addEventListener("progress", (event) => {
        if (event.lengthComputable) {
          const percent = (event.loaded / event.total) * 100;
          const progressText = "Your image is being uploded";

          progressBox.innerHTML =
            `<span style = "text-align : center"><p>${progressText}</p></span>` +
            `<div class="progress">
                <div class="progress-bar" role="progressbar" style="width: ${percent}%;" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100">
                      ${percent.toFixed(1)}%
                </div>
            </div>`;
        }
      });

      return xhr;
    },
    success: function () {
      document.getElementById("upload-btn").style.display = "none";
      progressBox.classList.add("not-visible");
      submitBtn.innerHTML = `<input type="submit" value="CHECK RESULT">`;

      alertBox.innerHTML =
        `<p style="display:inline-block;margin: right 5px;">Image uploaded Successfully</p>` +
        `<img src=${gifUrl} alt="Done" style="width: 16px; height: 16px; display:inline-block;">`;

      imageBox.innerHTML = `<img src="${url}" style = "width : 300px; height : auto; object-fit: contain; display: block; margin: 0 auto; padding-top:0px;">`;
    },
    error: function (error) {
      console.log(error);
      progressBox.classList.add("not-visible");
      alertBox.innerHTML = `<div class="alert alert-danger text-center" role="alert">
        Oops something went wrong!
      </div>`;
    },
    cache: false,
    contentType: false,
    processData: false,
  });
});

/* Submit the Form
$("#upload-form").bind("submit", function (event) {
  $.ajax({
    type: $(this).attr("method"),
    url: $(this).attr("action"),
    data: {
      image: $("#id_image").val(),
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      action: "post",
    },
  });
  event.preventDefault();
  return false;
}); */
