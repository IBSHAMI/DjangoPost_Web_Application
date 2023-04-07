<template>
  <div>
    <div>
      <shared-component-profile-upload-error
        :uploadError="uploadError"
        :uploadErrorMessage="uploadErrorMessage"
        @closeErrorAlert="closeErrorAlert"
      />
      <div class="card">
        <div class="card-title">
          <div class="d-flex justify-content-between p-2 mx-2">
            <span class="ml-auto">Upload Logo</span>
            <button
              class="btn btn-close ml-auto"
              style="cursor: pointer"
              @click.prevent="CloseUploadModel"
            ></button>
          </div>
        </div>

        <div class="card-body">
          <!-- Upload Dropbox -->
          <div
            class="w-100 h-100 py-5 rounded text-center cursor-pointer border border-dashed transition duration-500 hover:bg-primary hover:text-white"
            :class="{
              'bg-success text-white': isDragActive,
            }"
            @darg.prevent.stop=""
            @dragstart.prevent.stop=""
            @dragend.prevent.stop="dragEnd"
            @dragover.prevent.stop="dragStart"
            @dragenter.prevent.stop="dragStart"
            @dragleave.prevent.stop="dragEnd"
            @drop.prevent.stop="upload($event)"
          >
            <h5 v-if="!fileName">Drop your logo here</h5>
            <h5 v-else>Logo uploaded!!</h5>
          </div>
          <div class="text-center my-3">
            <label for="file-upload" class="btn btn-primary">
              Upload Logo
            </label>
            <input
              id="file-upload"
              type="file"
              class="d-none"
              @change="upload($event, true)"
              accept="image/jpeg, image/png"
            />
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
    upload(event, isFileInput = false) {
      this.dragEnd();

      let file;

      if (isFileInput) {
        file = [...event.target.files];
      } else {
        file = [...event.dataTransfer.files];
      }

      if (file.length > 1) {
        this.uploadErrorHandle("You can only upload one image file");
        return;
      }

      if (file[0].type === "image/png" || file[0].type === "image/jpeg") {
        this.fileName = file[0].name;
        this.closeErrorAlert();
        this.$emit("upload", file);
      } else {
        this.uploadErrorHandle("You can only upload png or jpeg images");
      }
    },
  },
};
</script>

<style></style>
