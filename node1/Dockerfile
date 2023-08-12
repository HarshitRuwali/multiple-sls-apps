FROM --platform=linux/amd64 public.ecr.aws/lambda/nodejs:16

COPY app.js ./

# You can overwrite command in `serverless.yml` template
CMD ["app.handler"]
