<template>
  <div class="col-span-1">
    <div class="bg-white rounded border border-gray-200 relative flex flex-col">
      <div
        class="text-white px-6 py-4 border-0 rounded relative mb-4 bg-rose-500"
        v-show="uploadError"
      >
        <span class="text-xl inline-block mr-5 align-middle">
          <i class="fas fa-bell" />
        </span>
        <span class="inline-block align-middle mr-8">
          <b class="capitalize">Error!</b> {{ uploadErrorMessage }}
        </span>
        <div
          class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
          style="cursor: pointer"
          @click.prevent="closeErrorAlert"
        >
          <span>×</span>
        </div>
      </div>
      <div class="px-6 pt-6 pb-5 font-bold border-b border-gray-200">
        <span class="card-title">Upload Logo</span>
        <div
          class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
          style="cursor: pointer"
          @click.prevent="CloseUploadModel"
        >
          <span>×</span>
        </div>
        <i class="fas fa-upload float-right text-green-400 text-2xl"></i>
      </div>
      <div class="p-6">
        <!-- Upload Dropbox -->
        <div
          class="w-full px-10 py-20 rounded text-center cursor-pointer border border-dashed border-gray-400 text-gray-400 transition duration-500 hover:text-white hover:bg-green-400 hover:border-green-400 hover:border-solid"
          :class="{
            'bg-green-400 text-white border-green-400 border-solid':
              isDragActive,
          }"
          @darg.prevent.stop=""
          @dragstart.prevent.stop=""
          @dragend.prevent.stop="dragEnd"
          @dragover.prevent.stop="dragStart"
          @dragenter.prevent.stop="dragStart"
          @dragleave.prevent.stop="dragEnd"
          @drop.prevent.stop="upload($event)"
        >
          <h5>Drop your files here</h5>
        </div>
        <hr class="my-6" />
        <!-- Progess Bars -->
        <div class="mb-4">
          <!-- File Name -->
          <div class="font-bold text-sm" v-html="fileName"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CompanyLogoUpload",
  data() {
    return {
      isDragActive: false,
      uploadError: false,
      uploadErrorMessage: "",
      fileName: "",
    };
  },
  methods: {
    dragStart() {
      this.isDragActive = true;
    },
    dragEnd() {
      this.isDragActive = false;
    },
    uploadErrorHandle(error) {
      this.uploadError = true;
      this.uploadErrorMessage = error;
    },
    closeErrorAlert() {
      this.uploadError = false;
      this.uploadErrorMessage = "";
    },
    CloseUploadModel() {
      this.$emit("closeUploadModel");
    },
    upload($event) {
      // Disable the active drop styles
      this.dragEnd();

      // Get the files from the event
      const file = [...$event.dataTransfer.files];

      // check if the file is pdf
      if (file.length > 1) {
        // Upload the file
        this.uploadErrorHandle("You can only upload one file");
        return;
      }
      if (file[0].type === "image/png" || file[0].type === "image/jpeg") {
        // Get the file name
        this.fileName = file[0].name;
        this.closeErrorAlert();
        this.$emit("upload", file);
      } else {
        console.log(file[0].type);
        this.uploadErrorHandle("You can only upload png or jpeg images");
      }
    },
  },
};
</script>

<style></style>
