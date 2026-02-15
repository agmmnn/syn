import index from "./index.html";

const isDev = process.env.NODE_ENV !== "production";

Bun.serve({
  port: 3000,
  hostname: "0.0.0.0",
  routes: {
    "/": index,
  },
  development: isDev ? { hmr: true, console: true } : false,
});

console.log("syn web → http://localhost:3000");
