/**
 *Load DOM elements first
 **/
document.addEventListener("DOMContentLoaded", function () {
  initiateModalImages();
  executeFunctionAfterTime(removeSuccessDiv, 3000);
});

/**
 *Function that creates a modal with properties
 **/
function createModal() {
  let modal = new bootstrap.Modal(document.querySelector("#img-modal"), {
    keyboard: false,
    backdrop: "static",
  });
  modal.show();
}

/**
 *Replace modal src attribute with different image src
 **/
function imageSrcReplacer(imageCandidate) {
  let imageCandidateSrc = imageCandidate.getAttribute("src");
  let imgModal = document.querySelector("#modal-img");
  imgModal.src = imageCandidateSrc;
  createModal();
}

/**
 *Add event listeners for modal images
 **/
function initiateModalImages() {
  let images = document.querySelectorAll(".gallery-image");
  for (let image of images) {
    image.addEventListener("click", function () {
      imageSrcReplacer(image);
    });
  }
}

/**
 *Function that executes function after time
 **/
function executeFunctionAfterTime(functionToExecute, time) {
  setTimeout(functionToExecute, time);
}

/**
 *Remove SuccessDiv if it exists
 **/
function removeSuccessDiv() {
  let targetedDiv = document.getElementById("success_message");
  if (targetedDiv) {
    targetedDiv.remove();
  }
}
