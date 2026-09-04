import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

interface ApiNode {
  id: string;
  type: string;
  meta?: Record<string, unknown>;
}

interface CourseApi {
  course: { code: string };
  nodes: ApiNode[];
}

const api = JSON.parse(readFileSync(resolve("dist/api/index.json"), "utf8")) as CourseApi;
const nodesOf = (type: string) => api.nodes.filter((n) => n.type === type);

describe("assignment 2 brief", () => {
  it("keeps the three digits the repo arrived with in the SLOP code", () => {
    expect(api.course.code).toMatch(/^SLOP[1234368]555$/);
  });

  it("runs across twelve dated teaching weeks", () => {
    const weeks = new Set(nodesOf("sessions").map((n) => n.meta?.week));
    for (let week = 1; week <= 12; week += 1) {
      expect(weeks.has(week), `no session scheduled for week ${week}`).toBe(true);
    }
  });

  it("has at least one lecture linking to a deck that actually exists", () => {
    const withSlides = nodesOf("lectures").filter((n) => typeof n.meta?.slides === "string");
    expect(withSlides.length, "no lecture has a slides: link").toBeGreaterThan(0);
    for (const lecture of withSlides) {
      const path = resolve("dist", (lecture.meta?.slides as string).replace(/^\//, ""), "index.html");
      expect(existsDeckPage(path), `${lecture.id} links to a deck that didn't build`).toBe(true);
    }
  });

  it("has assessment weights that add up to 100", () => {
    const total = nodesOf("assessments").reduce(
      (sum, n) => sum + (Number(n.meta?.weight) || 0),
      0,
    );
    expect(total).toBe(100);
  });

  it("still ships the fixed Slop brand palette (never mine to touch)", () => {
    // The theme injects brandCss as an unlayered inline <style> in <head>, so
    // it overrides the theme's own @layer'd defaults regardless of the
    // external stylesheet's load order — check the page, not the bundled CSS.
    const home = readFileSync(resolve("dist/index.html"), "utf8");
    expect(home, "brand token --at-primary missing from the page").toContain("--at-primary:#b97d1c");
  });
});

function existsDeckPage(path: string): boolean {
  try {
    readFileSync(path);
    return true;
  } catch {
    return false;
  }
}
