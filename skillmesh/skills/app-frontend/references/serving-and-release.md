# Verify the intended serving configuration

Read this when hosting, production assets or deployment preparation are in scope. Establish the actual host and topology first; development rendering does not establish production behavior.

## Prepare within the owner's release controls

Release compilation, bundling, publishing and deployment are owner-initiated by default. Prepare explicit build settings and commands without silently invoking them or adding publish hooks. An explicit build request authorizes that artifact within scope; ordinary development builds/tests remain implementation verification. If the owner has neither produced nor authorized the bundle, keep production checks pending and continue independent work.

For owner-selected IIS hosting, prepare pinned toolchain/dependencies, the production build command and output directory, public configuration, API/base-path settings, IIS configuration and operator verification/recovery steps. The owner builds, inspects and deploys unless execution is explicitly delegated. Do not assume IIS or separate sites for another project.

## Make the serving responsibilities explicit

Distinguish static browser assets from SSR/server output, which needs its supported runtime. A standalone static site needs its own hosting configuration. Assets bundled with ASP.NET Core must preserve the backend-generated web.config and be copied explicitly before the owner's backend publish step, without hidden hooks. Keep server secrets out of browser bundles and public configuration.

Record who serves navigation, API routes and missing assets. SPA fallback must not turn missing JavaScript or API failures into successful HTML responses. Account for base paths, deep links, asset loading, cache/version transitions, authentication and security headers under the actual topology.

## Exercise the produced candidate

When integration is material, exercise a representative real journey against the production bundle and intended serving/security configuration early, once an artifact is available or generation is authorized. Development or mock rendering can miss asset, CSP and authentication failures. Validate recovery as well as successful loading and API use.

Preserve useful assertions as project tests as implementation grows. Record candidate, host/configuration and observed results; put unavailable production, browser or identity proof beside the claims it limits. An available recipe is not a verified bundle or deployment.
