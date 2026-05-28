import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = "/Users/alex-lirio-lucian/develop/WaterUse-alex/LLM_Prompting";
const workbookPath = path.join(root, "ODD_EV-parking", "ODD_EV-parking.xlsx");
const previewPath = path.join(root, "ODD_EV-parking", "build", "ODD_EV-parking-preview.png");

const file = await FileBlob.load(workbookPath);
const workbook = await SpreadsheetFile.importXlsx(file);

for (const range of ["Sheet1!A1:B8", "Sheet1!A19:B25", "Sheet1!A75:B81"]) {
  const table = await workbook.inspect({
    kind: "table",
    range,
    include: "values,formulas",
    tableMaxRows: 12,
    tableMaxCols: 2,
  });
  console.log(`\n${range}`);
  console.log(table.ndjson);
}

const expectedAsTable = await workbook.inspect({
  kind: "table",
  range: "Expected AS!A1:E10",
  include: "values,formulas",
  tableMaxRows: 12,
  tableMaxCols: 5,
});
console.log("\nExpected AS!A1:E10");
console.log(expectedAsTable.ndjson);

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
console.log("\nFormula/error scan");
console.log(errors.ndjson);

const rendered = await workbook.render({ sheetName: "Sheet1", range: "A1:B81", format: "png", scale: 1 });
await fs.writeFile(previewPath, Buffer.from(await rendered.arrayBuffer()));
console.log(`\nRendered preview: ${previewPath}`);
