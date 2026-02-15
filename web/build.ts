import { readFileSync, writeFileSync } from "fs";

const result = await Bun.build({
  entrypoints: ["./frontend.tsx"],
  outdir: "./dist",
  minify: true,
});

if (!result.success) {
  console.error("Build failed:", result.logs);
  process.exit(1);
}

const jsFile = result.outputs.find((o) => o.path.endsWith(".js"));
const cssFile = result.outputs.find((o) => o.path.endsWith(".css"));

if (!jsFile) {
  console.error("No JS output found");
  process.exit(1);
}

const jsFilename = jsFile.path.split("/").pop();
const cssFilename = cssFile?.path.split("/").pop();

let html = readFileSync("./index.html", "utf-8");

// Replace tsx script with built JS bundle
html = html.replace(
  `<script type="module" src="./frontend.tsx"></script>`,
  `<script type="module" src="./${jsFilename}"></script>`,
);

// Inject CSS link if Bun extracted a CSS file
if (cssFilename) {
  html = html.replace(
    `</head>`,
    `  <link rel="stylesheet" href="./${cssFilename}" />\n  </head>`,
  );
}

writeFileSync("./dist/index.html", html);
console.log("Build complete → dist/");
