import upperFirst from "lodash/upperFirst";
import camelCase from "lodash/camelCase";

export default {
  install(app) {
    // search for global components
    const sharedComponents = import.meta.glob(
      "../components/sharedComponents/*.vue",
      {
        // looks for all .vue files in the folder
        eager: true, // eager force the import of all files
      }
    );

    // loop to get the path and module (component file)
    Object.entries(sharedComponents).forEach(([path, module]) => {
      const componentName = upperFirst(
        camelCase(
          path
            .split("/")
            .pop()
            .replace(/\.\w+$/, "")
        )
      );

      app.component(`SharedComponent${componentName}`, module.default);
    });
  },
};
