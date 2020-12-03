FROM node:12-alpine as build

WORKDIR /app
RUN mkdir frontend
COPY package.json ./frontend/
COPY package-lock.json ./frontend/
RUN cd frontend && npm install --only=prod
COPY . ./frontend
RUN cd frontend && npm install && npm run build

FROM nginx:1.16.0-alpine
COPY --from=build /app/frontend/build /usr/share/nginx/html
COPY --from=build /app/frontend/nginx/default.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]
