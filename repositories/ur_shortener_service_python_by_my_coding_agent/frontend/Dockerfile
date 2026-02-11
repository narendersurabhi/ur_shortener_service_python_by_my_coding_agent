# Multi-stage build for a typical Node.js frontend (e.g. Create React App)
FROM node:18-alpine AS build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package*.json ./
RUN npm ci --silent
COPY . .
# build script should produce a "build" directory (CRA) or be a no-op if not present
RUN npm run build --if-present

FROM nginx:alpine
# Copy built static assets (expects /app/build)
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]