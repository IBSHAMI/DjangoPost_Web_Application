<template>
  <div>
    <div>
      <div class="md:grid md:grid-cols-3 md:gap-6">
        <div class="md:col-span-1">
          <div class="px-4 sm:px-0">
            <h3 class="text-lg font-medium leading-6 text-gray-900">Profile</h3>
            <p class="mt-1 text-sm text-gray-600">
              This information will be displayed publicly so be careful what you
              share.
            </p>
          </div>
        </div>
        <div class="mt-5 md:col-span-2 md:mt-0">
          <form action="#" method="POST">
            <div class="shadow sm:overflow-hidden sm:rounded-md">
              <div class="space-y-6 bg-white px-4 py-5 sm:p-6">
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >First Name</label
                    >
                    <div class="w-full h-full relative mt-1 py-2">
                      <input
                        type="text"
                        name="price"
                        id="price"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-800 focus:ring-indigo-800 sm:text-sm"
                        placeholder="0.00"
                      />
                    </div>
                  </div>
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="company-website"
                      class="block text-base font-medium text-gray-700"
                      >Last Name</label
                    >
                    <div class="mt-1 w-full h-full flex py-2">
                      <input
                        type="text"
                        name="company-website"
                        id="company-website"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        placeholder=""
                      />
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >Email</label
                    >
                    <div class="w-full h-full relative mt-1 py-2">
                      <input
                        type="text"
                        name="price"
                        id="price"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        placeholder="0.00"
                      />
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >Software Field</label
                    >
                    <div class="w-full h-full relative mt-1 py-2">
                      <input
                        type="text"
                        name="price"
                        id="price"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        placeholder="0.00"
                      />
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >Expected Salary</label
                    >
                    <div class="w-full h-full relative mt-1 py-2">
                      <div
                        class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3"
                      >
                        <span class="text-gray-500 sm:text-sm">$</span>
                      </div>
                      <input
                        type="text"
                        name="price"
                        id="price"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        placeholder="0.00"
                      />
                      <div class="absolute inset-y-0 right-0 flex items-center">
                        <label for="currency" class="sr-only">Currency</label>
                        <select
                          id="currency"
                          name="currency"
                          class="h-full rounded-md border-transparent bg-transparent py-0 pl-2 pr-7 text-gray-500 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        >
                          <option>USD</option>
                          <option>MYR</option>
                        </select>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="company-website"
                      class="block text-base font-medium text-gray-700"
                      >Linkedin Profile</label
                    >
                    <div class="mt-1 w-full h-full flex py-2">
                      <span
                        class="block h-full inline-flex items-center rounded-l-md border border-r-0 border-gray-300 bg-gray-50 px-3 text-sm text-gray-500"
                        >http://</span
                      >
                      <input
                        type="text"
                        name="company-website"
                        id="company-website"
                        class="block w-full h-full flex-1 rounded-none rounded-r-md border-2 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        placeholder="www.example.com"
                      />
                    </div>
                  </div>
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="company-website"
                      class="block text-base font-medium text-gray-700"
                      >Portfolio Website</label
                    >
                    <div class="mt-1 w-full h-full flex py-2">
                      <span
                        class="block inline-flex items-center rounded-l-md border border-r-0 border-2 bg-gray-50 px-3 text-sm text-gray-500"
                        >http://</span
                      >
                      <input
                        type="text"
                        name="company-website"
                        id="company-website"
                        class="block w-full flex-1 rounded-none rounded-r-md border-2 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        placeholder="www.example.com"
                      />
                    </div>
                  </div>
                </div>
                <div>
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >About</label
                    >
                    <div class="w-full h-full relative mt-1 py-2">
                      <textarea
                        id="about"
                        name="about"
                        rows="3"
                        class="mt-1 block w-full rounded-md border-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        placeholder="you@example.com"
                      ></textarea>
                    </div>
                  </div>
                </div>
                <div>
                  <label
                    class="block text-sm text-base font-medium text-gray-700"
                    >Upload Resume</label
                  >
                  <div class="mt-1 flex items-center py-2">
                    <input
                      type="file"
                      id="Upload Photo"
                      name="Upload Photo"
                      class="ml-5 rounded-md border border-gray-300 bg-white py-2 px-3 text-sm font-medium leading-4 text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                    />
                  </div>
                </div>
                <div>
                  <label
                    class="block text-sm text-base font-medium text-gray-700"
                    >Upload Profile Photo</label
                  >
                  <div class="mt-1 flex items-center py-2">
                    <input
                      type="file"
                      id="Upload Photo"
                      name="Upload Photo"
                      class="ml-5 rounded-md border border-gray-300 bg-white py-2 px-3 text-sm font-medium leading-4 text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                    />
                  </div>
                </div>
              </div>
              <div class="bg-gray-50 px-4 py-3 text-right sm:px-6">
                <button
                  type="submit"
                  class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                >
                  Save
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>

    <div class="hidden sm:block" aria-hidden="true">
      <div class="py-5">
        <div class="border-t border-gray-200"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileData",
};
</script>
