/// <reference types="cypress" />

describe("Test Access Your Information Flow", () => {
  beforeEach(() => {
    cy.login();
    cy.fixture("login_fixture").as("user");
  });

  it("Go through AYI Flow", function () {
    cy.visit("/pro/account/access/");
    cy.get("input[type=submit]").click();
    cy.contains('PENDING').should('be.visible');
    cy.reload();
    cy.get('a').contains("download").should('be.visible');
  });
});
