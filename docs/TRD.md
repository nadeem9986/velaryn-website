# Velaryn Website TRD

## 1. Technical Overview

The first Velaryn website should be a high-quality static or mostly static single-page marketing site for `velaryn.in`. It should be optimized for credibility, speed, SEO, accessibility, and future maintainability.

The site does not need a custom backend for version 1 unless a working contact form is required. Initial contact can use `mailto:contact@velaryn.in` or a lightweight form service added later.

## 2. Recommended Stack

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- Framer Motion

### UI

- shadcn/ui or local reusable components
- Radix UI primitives where needed
- Lucide icons

### Hosting

- Vercel for frontend hosting
- Domain: `velaryn.in`

### Optional Later Services

- Contact form provider or serverless API route
- Analytics with privacy-conscious configuration
- CMS for blog or company updates
- Firebase, Supabase, or PostgreSQL-backed services only when dynamic features are required

## 3. Architecture Principles

- Start with a single-page site.
- Keep content data easy to update.
- Separate section content from reusable UI components.
- Avoid adding backend complexity before it is needed.
- Keep product claims editable as Velaryn matures.
- Build the design system so future pages can reuse the same components.

## 4. Application Structure

Recommended structure for a Next.js implementation:

```text
app/
  layout.tsx
  page.tsx
  globals.css
components/
  layout/
  sections/
  ui/
content/
  homepage.ts
lib/
  constants.ts
  utils.ts
public/
  assets/
```

### Section Components

Suggested homepage sections:

- `Navbar`
- `HeroSection`
- `FocusStrip`
- `AboutSection`
- `MissionVisionSection`
- `CapabilitiesSection`
- `ProductsSection`
- `TechnologySection`
- `IndustriesSection`
- `WhyVelarynSection`
- `RoadmapSection`
- `FoundersSection`
- `CareersSection`
- `FAQSection`
- `ContactSection`
- `Footer`

## 5. Content Model

Content should be stored in structured constants so wording can be updated without digging through component layout logic.

Example content groups:

- Navigation links
- Focus areas
- Capabilities
- Products and initiatives
- Technologies
- Industries
- Roadmap phases
- Founders
- FAQ entries
- Contact details

## 6. UX Requirements

- First viewport must clearly show Velaryn as the brand.
- Navigation should be sticky and readable over a dark background.
- Mobile navigation should be compact and accessible.
- CTAs should scroll to relevant sections or open email.
- Product cards should show status labels clearly.
- Rescue Call should appear as an in-development initiative, not as the whole company.
- Founders section should mention names only until bios and official profiles are ready.

## 7. Visual Requirements

- Dark premium background.
- Subtle aurora gradients.
- Glass-style cards with controlled transparency.
- Bento-style layouts for company values and capabilities.
- Abstract real-time systems visual, network, globe, or map-inspired scene.
- Avoid stock photos in the first version.
- Avoid exaggerated visual effects that reduce trust.

## 8. Animation Requirements

Recommended animation behavior:

- Fade-up section reveals.
- Subtle parallax on background gradients.
- Gentle card hover states.
- Smooth scrolling to sections.
- Animated network or abstract system visual in hero.
- Reduced-motion support for users who prefer less animation.

Do not animate critical text in a way that makes it hard to read.

## 9. SEO Requirements

Minimum SEO metadata:

- Title: `Velaryn | Technology for Critical Moments`
- Description: `Velaryn is an emerging technology startup building intelligent software for emergency response, healthcare coordination, and mission-critical operations.`
- Canonical domain: `https://velaryn.in`
- Open Graph title, description, and image
- Twitter card metadata
- Sitemap
- Robots file

Recommended structured data:

- Organization schema with careful early-stage wording
- Website schema

Avoid claiming official registration details until confirmed.

## 10. Accessibility Requirements

- Semantic HTML sections.
- Keyboard-accessible navigation.
- Visible focus states.
- Sufficient contrast.
- Proper heading hierarchy.
- Descriptive labels for icon buttons.
- Reduced-motion support.
- Forms, if added, must have labels and validation states.

## 11. Performance Requirements

Targets:

- Lighthouse performance score: 90+
- Lighthouse accessibility score: 95+
- Lighthouse best practices score: 95+
- Lighthouse SEO score: 95+

Implementation guidance:

- Avoid heavy animation libraries beyond what is necessary.
- Optimize images and generated assets.
- Use CSS effects carefully.
- Keep JavaScript bundle size low.
- Lazy-load non-critical visuals if needed.

## 12. Contact Handling

Version 1 option:

- `mailto:contact@velaryn.in`

Version 2 option:

- Contact form submitted through a serverless API route or external form provider.
- Spam protection.
- Email notification to `contact@velaryn.in`.
- Clear success and error states.

## 13. Analytics

Optional for launch:

- Vercel Analytics or privacy-conscious analytics.
- Track only basic page engagement.
- Avoid collecting sensitive user data.

## 14. Deployment

Recommended deployment flow:

1. Build site locally.
2. Run linting and production build.
3. Deploy to Vercel.
4. Connect `velaryn.in`.
5. Configure DNS.
6. Verify HTTPS.
7. Test mobile and desktop layouts.
8. Submit sitemap after launch.

## 15. Risks

| Risk | Mitigation |
| --- | --- |
| Website overclaims company maturity | Use early-stage wording and status labels |
| Design looks too flashy for emergency technology | Keep visual effects subtle and trust-focused |
| Contact email not active at launch | Confirm email setup before publishing |
| Social links unavailable | Omit links until official accounts exist |
| Future product details change | Keep content centralized and easy to update |

## 16. Future Expansion

Possible later additions:

- Separate product page for Rescue Call.
- Blog or engineering updates.
- Careers page.
- Investor or partner inquiry form.
- Product waitlist.
- Case studies once real partners exist.
- Official legal pages after company registration.
