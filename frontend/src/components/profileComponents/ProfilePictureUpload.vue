<template>
  <div class="col-span-1">
    <div class="bg-white rounded border border-gray-200 relative flex flex-col">
      <profile-upload-error
        :uploadError="uploadError"
        :uploadErrorMessage="uploadErrorMessage"
        @closeErrorAlert="closeErrorAlert"
      />
      <div class="card">
        <div class="card-title">
          <div class="d-flex justify-content-between p-2 mx-2">
            <span class="ml-auto">Upload Profile Picture</span>
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
            <h5 v-if="!fileName">Drop your picture here</h5>
            <h5 v-else>Picture uploaded!!</h5>
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
import ProfileUploadError from "@/components/profileComponents/ProfileUploadError.vue";

export default {
  name: "ProfilePictureUpload",
  data() {
    return {
      isDragActive: false,
      uploadError: false,
      uploadErrorMessage: "",
      fileName: "",
    };
  },
  components: {
    ProfileUploadError,
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
      this.$emit("closeUploadModel", "picture_model");
    },
    upload($event) {
      // Disable the active drop styles
      this.dragEnd();

      // Get the files from the event
      const file = [...$event.dataTransfer.files];

      // check if the file is pdf
      if (file.length > 1) {
        // Upload the file
        this.uploadErrorHandle("You can only upload one pdf file");
        return;
      }
      if (file[0].type === "image/png" || file[0].type === "image/jpeg") {
        // Get the file name
        this.fileName = file[0].name;
        this.closeErrorAlert();
        this.$emit("upload", file, "picture");
      } else {
        console.log(file[0].type);
        this.uploadErrorHandle("You can only upload png or jpeg images");
      }
    },
  },
};
</script>

<style></style>
