import HomeView from "@/views/HomeView.vue";
import { describe, test, expect } from "vitest";
import { mount } from "@vue/test-utils";

describe("Landing page", () => {
  test("renders correctly", () => {
    const wrapper = mount(HomeView);
    expect(wrapper.text()).toContain("Welcome to DjangoPost");
  });
});
